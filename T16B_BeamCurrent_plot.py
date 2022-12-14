import datetime
import math
import os
import random
import sys
import time
import traceback
import pandas as pd
# change to Qt6 for python PySide6 and Python310--start_date 2022/07/06
import PySide6
import serial
import serial.tools.list_ports
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize, Qt, QThread, QTimer, Signal, Slot
from PySide6.QtGui import (QAction, QDoubleValidator, QIcon, QIntValidator,
                           QTextCursor)
from PySide6.QtWidgets import (QApplication, QFileDialog, QGridLayout,
                               QMainWindow, QMessageBox, QPushButton, QStyle,
                               QWidget)
from serial import SerialException
# Pyepics for epics access 
from epics import (ca, caget, cainfo, camonitor, caput, PV, camonitor_clear,
                 get_pv)
# import data form to save dict data
from Dependant.Dict_DataFrame_Sqlite import (dict_to_csv, dict_to_excel,
                                             dict_to_json, dict_to_SQLTable)
# import my own matplotlib InitialPlot
from Dependant.My_Matplotlib_PySide6 import (InitialPlot, MonitorPlot, Myplot,
                                             NavigationToolbar)
# import my tool functions for usage
from Dependant.Tools_functions import (creatPath, deco_count_time,
                                       get_datetime, log_exception,
                                       log_exceptions, my_logger, to_log)
# import read thread for pAmeter 6517B
#from Linkage.Keithley_pAmeter_driver import Read6517bCurrent
from Linkage.Keithley_pA6485_driver_R232 import Keithley6485Com, get_COM_port
#from Linkage.PMC_motor_driver import pmc, pmcSetThread
from Linkage.Mono_control import PVmotorThread
# import scan channel info
from Linkage.EPICS_PV_names_T16B import FULL_Channels
# import data view plot UI
from UI.Data_View_Plot import DataViewPlot
# import scan range UI
from UI.Input_scan_range import InputScanRange, calculate_scan_range
# import sub UI files
# import my message box
from UI.QtforPython_useful_tools import EmittingStr, MyMsgBox
from UI.SQLDataViewPlot import ViewSQLiteData
# import main UI function
from UI.UI_BPM_plot import Ui_MainWindow

# set up the host and port of the ethernet device for E-1608
# PD_host = '169.254.111.100'
PMC_host = '192.168.1.55'
PMC_port = 7777

# pAmeter RS485_To_ethernet address
HOST = '10.30.95.170'
Port_list = [23, 26, 29, 32]  # port in USR_N540
pA_address = (HOST, Port_list[1])
# pA_PORT=TelnetAdapter(HOST,Port_list[1]) # for connection via USR450_To_RS232/485
pA_PORT = 'ASRL6::INSTR'  # for direct connection via RS232/485
pA6485_port='Com5'
file_path=os.getcwd()
# save path info
save_path = os.path.join(file_path, 'save_data')
creatPath(save_path)
# sqlite database path
SQLiteDB_path=save_path
MT_save_path = os.path.join(file_path, 'MT_data')
creatPath(MT_save_path)
log_path = os.path.join(file_path, 'log_info')
creatPath(log_path)

# logger
log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Limin')

"""
notes:
This is the main python file for  plotting the < X/Z position vs I_V_PD>, and then determine the beam size 
# Data structure
full_data = {'BPM-X pos(um)': self._plot_X_list, 'BPM-Z pos(um)': self._plot_Z_list,
            'adc voltage(V)': self._plot_adc_list, 'current(pA)': self._plot_pAmeter_list,
            'time_stamp': self._time_stamp, 'scan set': self._scan_list}
"""


# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************


class BeamMotionPlot(QMainWindow, Ui_MainWindow):
    # signal used
    scan_info_sig = Signal(dict)
    scan_start_sig = Signal(list)

    @log_exceptions(log_func=logger.error)
    def __init__(self, parent=None):
        super(BeamMotionPlot, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('RIXS@09_BeamSpot_plot')
        self.__ini_output()
        self.__init_plot__()
        self.__ini_pAmeter__()
        self._ini_menu()


    # def show_pAmeter_status(self, check):
    #     timeout = 1
    #     print(f'try connect pAmeter in {timeout}s...')
    #     pAmeter_status = ''
    #     current=0
    #     pA_info = f'pAmeter:keithley6517B\nhost: {HOST}\nPort_2:{Port_list[1]}'
    #     try:
    #         #self.pA_PORT = TelnetAdapter(HOST, Port_list[1], timeout=1)
    #         current=self.ini_keithley6517B_curr(nplc=1,points=5)
    #     except Exception as e:
    #         print(e)
    #         error_info = traceback.format_exc() + str(e) + '\n'
    #         logger.error(error_info)
    #         pAmeter_status = f' Not connected with timeout:{timeout}s'
    #     else:
    #         pAmeter_status = ' connected'
    #         self._pAmeter_started = True
    #     self.msg_box = MyMsgBox(title='pAmeter status', text=f'pAmeter' + pAmeter_status+f'\nget currents:{current:.4f}pA', details=pA_info)
    #     self.msg_box.show()


    # def ini_keithley6517B_curr(self,nplc=5,points=10):
    #     print('Start setting Keithley6517B....')
    #     t_start=time.time()
    #     Keithley6517B = Keithley6517BCom(address=(HOST, Port_list[1]), func='currents', points=points,nplc=nplc)
    #     ID = Keithley6517B.deviceID
    #     version = Keithley6517B.version
    #     print(f'get ID: {ID}\n version:{version}')
    #     #Keithley6517B.reset()
    #     Keithley6517B.clear_status()  # 1s
    #     Keithley6517B.configure_current() # 0.3s
    #     Keithley6517B.current_filter() # 1.2s
    #     Keithley6517B.initiate_continuous(continu=True) # 0.1s
    #     Keithley6517B.current_nplc(nplc=nplc) #1.0s
    #     Keithley6517B.curr_aver_counts(num=points) #0.1s
    #     Keithley6517B.zero_check(status='OFF') # 0.1s
    #     time.sleep(1+nplc/2) # 2s
    #     resp = Keithley6517B.fresh_data(wait=200) # 0.2s
    #     data = Keithley6517B.get_value(resp)*1e12
    #     print(f'set pAmeter done in {(time.time() - t_start):.2f} seconds ')
    #     return data
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    MenuBar part
    """
    @log_exceptions(log_func=logger.error)
    def _ini_menu(self):
        """
        for menuBar
        :return:
        """
        style = QApplication.style()
        # open data file
        OpenDATA = QAction('open data(&O)...', self)
        OpenDATA.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        OpenDATA.setShortcut(Qt.CTRL + Qt.Key_O)
        OpenDATA.triggered.connect(self.open_datafile)
        self.menuMenu.addAction(OpenDATA)
        # save data
        SaveDATA = QAction('save data(&S)...', self)
        SaveDATA.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        SaveDATA.setShortcut(Qt.CTRL + Qt.Key_S)
        SaveDATA.triggered.connect(self.save_all_data)
        self.menuMenu.addAction(SaveDATA)
        # show View data in analysis menuBar
        self.actionView_data.triggered.connect(self.show_full_data)
        self.actionDatabase.triggered.connect(self.view_sql_data)
        self.__init__Icons()

    @log_exceptions(log_func=logger.error)
    def __init__Icons(self):
        """Initial all icons in the menuBar"""
        #icon_path=os.path.join(os.getcwd(),'icons')
        icon_path=os.path.realpath('icons')
        print(f'icon_path: %s' % icon_path)
        data_icon=QIcon(os.path.join(icon_path, 'databricks.svg'))
        database_icon=QIcon(os.path.join(icon_path, 'datacamp.svg'))
        PMC_motor_icon=QIcon(os.path.join(icon_path, 'pkgsrc.svg'))
        pAmeter_icon=QIcon(os.path.join(icon_path, 'avast.svg'))
        self.actionView_data.setIcon(data_icon)
        self.actionDatabase.setIcon(database_icon)
        self.actionPMC_motor.setIcon(PMC_motor_icon)
        self.actionpAmeter.setIcon(pAmeter_icon)
        Eline_icon=QIcon(os.path.join(icon_path, 'databricks.svg')) #databricks
        #Eline_icon=QIcon(os.path.join(icon_path, 'Eline20U_icons.svg'))
        self.setWindowIcon(Eline_icon)
        self.setIconSize(QSize(80,80))
    
    @log_exceptions(log_func=logger.error)
    def open_datafile(self):
        """
        open data file,file format should be excel(.xlsx)
        :return:
        """
        pd_data = pd.DataFrame()
        filename, filetype = QFileDialog.getOpenFileName(self, "read data file(supported filetype:xlsx/csv/json)",
                                                         './', '*.xlsx;;*.csv;;*.json')
        print(filename, filetype)
        if filename.endswith('.xlsx'):
            # add dtype={'time stamp': 'datetime64[ns]'} if have 'time stamp'
            pd_data = pd.read_excel(filename, index_col=0, na_values=["NA"], engine='openpyxl')
            # print(pd_data)
        if filename.endswith('.csv'):
            pd_data = pd.read_csv(filename, index_col=0)
        if filename.endswith('.json'):
            pd_data = pd.read_json(filename)
        # drop the row with NaN and return
        valid_pd_data = pd_data
        self.ViewopenData = DataViewPlot(valid_pd_data)
        self.ViewopenData.show_data_table(valid_pd_data)
        self.ViewopenData.show()
    
    @log_exceptions(log_func=logger.error)
    def save_all_data(self):
        """
        save all data to usr defined location and name,
        file format should be excel(.xlsx)
        :return:
        """
        print('save data')
        scan_data = self.get_full_data()
        self.usr_save_full_data(scan_data, save_path, usr_define=1)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def view_sql_data(self):
        self.ViewSqlData = ViewSQLiteData()
        self.ViewSqlData.show()


    @log_exceptions(log_func=logger.error)
    def show_full_data(self):
        self.ViewData = DataViewPlot()
        full_dict_data = self.get_full_data()
        full_pd_data = self.ViewData.dict_to_pd(full_dict_data)
        self.ViewData.show_data_table(full_pd_data)
        self.ViewData.show()

    """
    end of MenuBar part
    """

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    @log_exceptions(log_func=logger.error)
    def __ini_output(self):
        # set a timer to show current time
        self.cur_timer = QTimer()
        self.cur_timer.timeout.connect(self.set_cur_time)
        self.cur_timer.start(100)
        # out put all to status_box
        sys.stdout = EmittingStr()
        sys.stderr = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)
        sys.stderr.textWritten.connect(self.outputWritten)
        # program start info
        start_info = f'Beam position plot program \n\tby Limin Zhou @SSRF_20U' \
                     f'\n\t{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}'
        print(start_info)

    # out put info into the status msg box
    def outputWritten(self, text):
        cursor = self.Msg_box.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.Msg_box.setTextCursor(cursor)
        self.Msg_box.ensureCursorVisible()

    def set_cur_time(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.Now_T.setText(f'Now: {timestamp}')

    # raise info part
    def raise_warning(self, text):
        return QMessageBox.warning(self, 'ERROR', text, QMessageBox.Yes | QMessageBox.Cancel)

    def raise_info(self, text):
        return QMessageBox.information(self, 'info', text, QMessageBox.Yes | QMessageBox.Cancel)

    @log_exceptions(log_func=logger.error)
    def __init_plot__(self):        # initialize BPM figure Myplot for usage
        self.figure = InitialPlot()
        # add NavigationToolbar in the figure (widgets)
        self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Plot_box)
        self.gridlayout.addWidget(self.figure)
        self.gridlayout.addWidget(self.fig_ntb)

        # initialize PD Monitor figure Myplot for pAmeter electrometer 6517B usage
        self.pAmeter_figure = MonitorPlot()
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.pAmeter_plot)
        self.gridlayout.addWidget(self.pAmeter_figure)
        # initialize PMC X position Monitor figure Myplot for usage
        self.ch_pos_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.ch_position)
        self.gridlayout.addWidget(self.ch_pos_figure)

        # initialize PMC Y position Monitor figure Myplot for usage
        self.X_pos_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.X_position)
        self.gridlayout.addWidget(self.X_pos_figure)

        # initialize PMZ Z position Monitor figure Myplot for usage
        self.Z_pos_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Z_position)
        self.gridlayout.addWidget(self.Z_pos_figure)
        # self.gridlayout.addWidget(self.fig_ntb)


    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the pA electrometer part
    """

    def __ini_pAmeter__(self):
        self._MT_pA_currents = []
        self._MT_pA_delay = []
        self._pA_monitor_flag = 0
        self._pA_start_t = 0
        self._MT_save_N=0
        self._pAmeter_started=False
        self.Selected_port=''
        # list all port
        self.pAmeter_connection = False
        self.list_all_COM_port()
        self._status_timer=QTimer() # status timer
        self._status_timer.timeout.connect(self.update_pAmeter_status)
        self._shining_flag=0 # for indicate pAmeter connection
        self.serial_port=None

    def list_all_COM_port(self):
        COM_ports = get_COM_port()
        print(COM_ports)
        for COM, port in COM_ports.items():
            self.Port_cbx.addItem(f'{COM}:{port}')

    @Slot()
    def on_Connect_pAmeter_btn_clicked(self):
        """connect pAmeter 6514

        Returns:
            _type_: _description_
        """
        if self.Port_cbx.currentText() and not self.pAmeter_connection:
            Selected_port = self.Port_cbx.currentText().split(':')[0]
            try:
                self.serial_port=serial.Serial(Selected_port)
                self.pAmeter6485 = Keithley6485Com(port=self.serial_port, func='currents', points=5,full_time=100,keep_on=0)
                #status = self.pAmeter6514.open_port(Selected_port)
                status = "OK"
                connection_msg = self.Port_cbx.currentText() + ':\n' + str(status)
                version=self.pAmeter6485.version
                print(f'get version: {version}')
            except Exception as e: 
                #pAmeter6514=None
                self._msgbox = MyMsgBox(title="Connection msg", text="Connection to Electrometer6514 Fail", details=connection_msg+traceback.format_exc() + str(e))
                self._msgbox.show()
            else:
                if status == "OK" and version:
                    self._msgbox = MyMsgBox(title="Connection msg", text="Connection to Electrometer6514 Success", details=connection_msg)
                    print(f'Electrometer6514 at {Selected_port}:connected')
                    self.pAmeter6514.clear_status()
                    #self.MT_pAmeter6514.zero_check(status='OFF')
                    time.sleep(0.5)
                    self.pAmeter6514.conf_function('current',wait=500)
                    self.Connect_pAmeter_btn.setEnabled(False)
                    self.Connect_pAmeter_btn.setText("Connected")
                    self.pAmeter_connection = True
                    self.Selected_port=Selected_port
                #self.pAmeter6514.close_port()
                    self._msgbox.show()
            self._status_timer.start(1000)
            #print(self.pAmeter6514)
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Port_cbx_currentIndexChanged(self):
        # choose another port
        Selected_port = self.Port_cbx.currentText().split(':')[0]
        print(Selected_port)
        if self.pAmeter_connection and not self.Connect_pAmeter_btn.isEnabled():
            # pump connected, should disconnect and enable connection button
            self.Connect_pAmeter_btn.setEnabled(True)
            self.pAmeter6514 = None
            self.pAmeter_connection = False
            self.Connect_pAmeter_btn.setText("Connect")
    @Slot()
    def update_pAmeter_status(self):
        if self.pAmeter_connection:
            self.Connect_pAmeter_btn.setText("Connected")
            if self._shining_flag==0:
                self.Connect_pAmeter_btn.setStyleSheet("QPushButton{background-color: rgb(0, 255, 127);color:rgb(255, 255, 255)}")
                self._shining_flag=1
            elif self._shining_flag==1:
                self.Connect_pAmeter_btn.setStyleSheet("QPushButton{background-color: rgb(0, 170, 127);color:rgb(255, 255, 255)}")
                self._shining_flag=0
        else:
            #self.Connect_pAmeter_btn.setStyleSheet("QPushButton{background-color: rgb(98, 98, 98)}")
            self.Connect_pAmeter_btn.setText("Connect6514")

    def ini_keithley6514_curr(self,nplc=5,points=10):
        if self.pAmeter_connection:
            self.pAmeter6514.zero_check(status='OFF')
            self.pAmeter6514.conf_function('current')
            resp = self.pAmeter6514.read_data(wait=100)
            data = self.pAmeter6514.get_value(resp)
            print(f'get value:{data:.4e}A')
        else:
            self._msgbox = MyMsgBox(
                    title="Connection msg", text="Electrometer6514  initialize Fail", details='should connect Electrometer6514 ')
            self._msgbox.show()


    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Monitor_pA_clicked(self):
        if self._pA_monitor_flag == 0:
            self.clear_MT_data()
            print('Start monitoring pAmeter')
            self._pA_start_t = time.time()
            try:
                self.MT_pAmeter6485 = Keithley6485Com(port=self.serial_port, func='currents', points=5,full_time=1000,keep_on=1)
                self.MT_pAmeter6485.data_sig.connect(self.get_pAmonitor_data)
                status='OK'
                print(status)
                if  status=='OK':
                    #self.ini_keithley6514_curr(nplc=5,points=10)
                    #self.MT_pAmeter6514.clear_status()
                    #self.MT_pAmeter6514.zero_check(status='OFF')
                    #self.MT_pAmeter6514.conf_function('current',wait=100)
                    resp = self.MT_pAmeter6485.read_data(wait=100)
                    data = self.MT_pAmeter6485.get_value(resp)
                    print(f'get value:{data:.4e}A')
            except Exception as e:
                print(e)
            else:
                self._pA_monitor_flag = 1
                self._pAmeter_started=True
                print(f"status:{status}")
                self.MT_pAmeter6514.start()
        else:
            self.raise_warning('already monitoring')


    # @log_exceptions(log_func=logger.error)
    @Slot(list)
    def get_pAmonitor_data(self, resp: list):
        """
        fix
        :param resp:
        :return:
        """
        # assert resp[-1] == 'OK', self.raise_warning('error in reading pAmeter')
        if resp[-1] == 'OK' or resp[0] == 0.0:
            #self.lcd_pA.display(resp[0] * 1.0e12)
            self.lcd_display(resp[0])
            self._MT_pA_currents.append(resp[0] * 1.0e12)
            self._MT_pA_delay.append(time.time() - self._pA_start_t)
            # plot the data [value,delays]
            plot_delay = self._MT_pA_delay
            plot_read = self._MT_pA_currents
            if len(self._MT_pA_currents) > 200:
                plot_delay = self._MT_pA_delay[-200:]
                plot_read = self._MT_pA_currents[-200:]
            # plot
            self.pAmeter_figure.axes.cla()
            self.pAmeter_figure.axes.plot(plot_delay, plot_read, '-oc', markersize=1)
            self.pAmeter_figure.axes.set_title("pAmeter read", fontsize=10, color='m')
            self.pAmeter_figure.axes.set_xlabel("Delay(s)", fontsize=10, color='m')
            self.pAmeter_figure.axes.set_ylabel("currents value", fontsize=10, color='m')
            self.pAmeter_figure.draw()

    def lcd_display(self,current:int|float):
        """display current by uA, nA or pA

        Args:
            current (_type_): _description_

        Returns:
            _type_: _description_
        """
        lcd_value=-1.0
        if current*1.0e6>=1:
            # > 1uA
            lcd_value=current*1.0e6
            self.Current_label.setText('uA')
        elif current*1.0e6<1 and current*1.0e9>=1:
            # 1nA~1uA
            lcd_value=current*1.0e9
            self.Current_label.setText('nA')
        else:
            # < 1nA
            lcd_value=current*1.0e12
            self.Current_label.setText('pA')
        self.lcd_pA.display(lcd_value)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Stop_Monitor_pA_clicked(self):
        if self._pA_monitor_flag == 1:
            print('stop monitor pAmeter')
            self.MT_pAmeter6514.data_sig.disconnect(self.get_pAmonitor_data)
            self.MT_pAmeter6514.__del__()
            self._pA_monitor_flag = 0
            # save monitor data
            full_data = {'pA_delay': self._MT_pA_delay, 'current(pA)': self._MT_pA_currents
                         }
            t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
            self._MT_save_N += 1
            filename = f'MT_pA_data_{t_stamp}_{self._MT_save_N}'
            folder = time.strftime('%Y-%m-%d', time.localtime())
            save_folder = creatPath(os.path.join(MT_save_path, folder))
            self.save_scan_data(full_data, save_folder, filename)
        else:
            self.raise_info('not monitoring')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Clear_Monitor_pA_clicked(self):
        self.clear_MT_data()
        if self._pA_monitor_flag == 1:
            self.MT_pAmeter6514.data_sig.disconnect(self.get_pAmonitor_data)
            self.MT_pAmeter6514.__del__()
            self._pA_monitor_flag = 0
        else:
            pass
    
    def clear_MT_data(self):
        self._MT_pA_delay = []
        self._MT_pA_currents = []
        self._pA_start_t = 0
        self.pAmeter_figure.axes.cla()
        self.pAmeter_figure.draw()
    """
    end of the pAmeter part
    """

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the ch X-Y-Z motor part
    """
    def _ini_channel_scan(self):
        # ini the channel scan part
        self.scan_channel_name=self.Channel_cbx.currentText()
        self.scan_channel=FULL_Channels.get(self.Channel_cbx.currentText(),None)
        self.Channel_cbx.currentIndexChanged['int'].connect(self.set_scan_channel)
        # for monitor data list
        self.pv_changed_Num:int=0
        self.pv_value_list=list()
        self.pv_num_list=list()
        self.pv_timestamps=list()
        self.ch_value_dict={}
        # step move
        self.step_ch_size=0
        self.Step_ch_pos.valueChanged.connect(self.get_ch_step)
        self.ch_pos_move_flag=False
        self.PVmonitoring_flag=False
        #for ch connection status
        self.ch_status_timer=QTimer() # status timer
        self.ch_status_timer.timeout.connect(self.update_ch_status)
        self.ch_shining_flag=0 # for indicate pmc connection

    @Slot()
    def on_Connect_ch_btn_clicked(self):
        self.set_scan_channel(0)

    @Slot()
    def update_ch_status(self):
        if self.PVmonitoring_flag:
            if self.ch_shining_flag==0:
                self.Connect_ch_btn.setStyleSheet("QPushButton{background-color: rgb(0, 255, 127);color:rgb(255, 255, 255)}")
                self.ch_shining_flag=1
            elif self.ch_shining_flag==1:
                self.Connect_ch_btn.setStyleSheet("QPushButton{background-color: rgb(0, 170, 127);color:rgb(255, 255, 255)}")
                self.ch_shining_flag=0
        else:
            pass

    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def set_scan_channel(self, n: int):
        """
        choose instrument to measure current
        :return:
        """
        self.Channel_tabs.setCurrentIndex(0)
        self.scan_channel_name=self.Channel_cbx.currentText()
        self.scan_channel=FULL_Channels.get(self.Channel_cbx.currentText(),None)
        if self.scan_channel:
            # basic PV names for ch set readback and motor moving status[optional]
            self.ch_PVset=self.scan_channel.get("PV_SET",None)
            self.ch_PVrbv=self.scan_channel.get("PV_RBV",None)
            self.ch_PVmovn=self.scan_channel.get("PV_Motor_MOVN",None)
            if self.ch_PVset and self.ch_PVrbv:
                self.monitor_ch_value(self.ch_PVrbv)
                self._scan_range_set_flag=0
        else:
            self.raise_warning(f"channel: {self.scan_channel_name} do not support!")          
        
    def monitor_ch_value(self,ch_pvname:str):
        """monitor the ch_name value and plot

        Args:
            ch_name (str): _description_
        """
        pv_setinfo=f'{ch_pvname} Monitor'
        try:
            self._pv=PV(ch_pvname,callback=self.pv_value_changed,connection_timeout=5)
            if self._pv.connect(timeout=5):
                value=self._pv.get()
                if value:
                    self.ch_current_value=value
                    self.lcd_ch_pos.display(value)
                    pv_setinfo+=' started'
            else:
                pv_setinfo+=' not connected'
        except Exception as e:
            print(traceback.format_exc() + str(e))
        else:
            self.PVmonitoring_flag=True
        finally:
            print(f'end PV:{ch_pvname} set \n{pv_setinfo}')
            self.statusbar.showMessage(pv_setinfo,5)

    def pv_value_changed(self,pvname=None,value=None,**kw):
        """
        read PV value readback
        update and plot
        """
        if value and pvname==self.ch_PVrbv:
            self.PV_value_input.setText(f'{value:.4f}')
            timestamp=get_datetime()
            self.pv_changed_Num+=1
            self.pv_value_list.append(float(value))
            self.pv_num_list.append(self.pv_changed_Num)
            self.pv_timestamps.append(timestamp)
            self.ch_value_dict[pvname]=value
            if self.pv_changed_Num>100:
                num_list=self.pv_num_list[-100:]
                value_list=self.pv_value_list[-100:]
                timestamps=self.pv_timestamps[-100:]
            else:
                num_list=self.pv_num_list
                value_list=self.pv_value_list
                timestamps=self.pv_timestamps
            # plot the changes
            if self.Plot_x_cbx.currentIndex()==0:
                self.plot_PV_data(num_list,value_list,self.pvname,'ChangeNum')
            else:
                temp_timestamps=pd.Series(timestamps)
                pd_timestamps=pd.to_datetime(temp_timestamps)
                pd_value_list=pd.Series(value_list)
                self.plot_PV_data(self.ch_pos_figure,pd_timestamps,pd_value_list,self.pvname,'Timestamp')

    def plot_PV_data(self,ch_figure, x_list: list, y_list: list, x_name: str, y_name: str):
        """
        plot Grating position based on list: [x_pos] and change list [x_num_list]
        :param x_pos:
        :param x_num_list:
        :return:
        """
        ch_figure.axes.cla()
        ch_figure.axes.plot(x_list, y_list, marker='o', markersize=1, markerfacecolor='orchid',
                                   markeredgecolor='orchid', linestyle='-', color='c')
        ch_figure.axes.set_xlabel(x_name, fontsize=10, color='m')
        ch_figure.axes.set_ylabel(y_name, fontsize=10, color='m')
        ch_figure.axes.set_title(self.tagname,color='#ff5500')
        ch_figure.axes.figure.autofmt_xdate(rotation=25)
        ch_figure.axes.draw()

    # for step size
    @Slot()
    def get_ch_step(self):
        """
        get Channel step size (um)
        :return:
        """
        self.step_ch_size = float(self.Step_ch_pos.text())
        print(f'set channel {self.scan_channel_name} step size to: {self.step_ch_size}')

    # for Channel step move
    @Slot()
    def on_ch_pos_left_clicked(self):
        """left clicked X pos move to current ch_value-ch_step
        """
        if self.PVmonitoring_flag and not self.ch_pos_move_flag:
            current_ch_pos=self.ch_value_dict[self.ch_PVrbv]
            new_pos=current_ch_pos-self.step_ch_size
            try:
                print(f'ch pos: {current_ch_pos} move {new_pos} right is plus')
                self.ch_Lset_thread = PVmotorThread(self.ch_PVset, new_pos, self.ch_PVrbv, self.ch_PVmovn, 1)
                self.ch_Lset_thread.done_signal.connect(self.ch_pos_set_done)
                self.ch_Lset_thread.start()
                self.ch_pos_move_flag = True
            except Exception as e:
                print(e)
                logger.error(traceback.format_exc() + str(e))
        else:
            self.raise_info('Channel not connected or last step not finished , will not move')

    @Slot()
    def on_ch_pos_right_clicked(self):
        """right clicked X pos move to current ch_value+ch_step
        """
        if self.PVmonitoring_flag and not self.ch_pos_move_flag:
            current_ch_pos=self.ch_value_dict[self.ch_PVrbv]
            new_pos=current_ch_pos+self.step_ch_size
            try:
                print(f'ch pos: {current_ch_pos} move {new_pos} right is plus')
                self.ch_Rset_thread = PVmotorThread(self.ch_PVset, new_pos, self.ch_PVrbv, self.ch_PVmovn, 1)
                self.ch_Rset_thread.done_signal.connect(self.ch_pos_set_done)
                self.ch_Rset_thread.start()
                self.ch_pos_move_flag = True
            except Exception as e:
                print(e)
                logger.error(traceback.format_exc() + str(e))
        else:
            self.raise_info('Channel not connected or last step not finished , will not move')

    @Slot(list)
    def ch_pos_set_done(self,resp:list):
        """ get the pmcX set info
        """
        self.ch_pos_move_flag=False
        print(f'{resp[-1]}\npos_now: {resp[0]} with set_pos: {resp[1]}')

    """
    end of the chanel set motor part 
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the PMC motion vs pAmeter plot part
    """

    def __ini_ch_plot__(self):
        # data structure for plot and save
        self._plot_ch_list = []
        self._plot_pAmeter_list = []
        self._time_stamp = []
        # min-max BPM X/Z axis position and step size (um)
        self._min_ch_pos = -100000
        self._max_ch_pos = 100000
        self._min_ch_step = 0.5
        self._max_ch_step = 1000
        # flag for status 1 is on , 0 is off
        self._start_plot_flag = 0
        self._scan_range_set_flag = 0
        self._scan_ch_flag = 0
        self._scan_list = []
        self._scan_list_num = 0  # number of scan list
        self._scan_N = 0  # index of scan list
        self._save_file_flag = 0
        self._save_N = 0  # index for save order
        self.scan_ch_num=None
        self._scan_info=[None,None]

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Input_scan_range_btn_clicked(self):
        """
        check which channel is chosen, get the scan range list and return
        :return: scan range list
        """
        self.scan_channel_name=self.Channel_cbx.currentText()
        self.scan_channel=FULL_Channels.get(self.Channel_cbx.currentText(),None)
        if self.scan_channel:
            # basic PV names for scan ch set readback and motor moving status[optional]
            self.scan_ch_PVset=self.scan_channel.get("PV_SET",None)
            self.scan_ch_PVrbv=self.scan_channel.get("PV_RBV",None)
            self.scan_ch_PVmovn=self.scan_channel.get("PV_Motor_MOVN",None)
            print(f'choose scan channel: {self.scan_channel_name}')
            input_info = f'scan channel: {self.scan_channel_name}\nCurrent value:\n{self.scan_channel_name}:' \
                        f'{self.ch_value_dict[self.scan_channel_name]}\nScan info:\n{self._scan_info[-1]}'
            self.inputRange_dialog = InputScanRange(f'{self.scan_channel_name}', input_info)
            self.inputRange_dialog.data_sig.connect(self.get_scan_range)
            self.inputRange_dialog.show()

    @Slot(list)
    def get_scan_range(self, scan_range_list: list):
        """
        get the scan range,\n
        scan range list: [scan_type,[min_E,min_E+1*step_E...max_E]] \n
        :return:
        """
        if scan_range_list[-1]:
            self._scan_info = scan_range_list
            self.raise_info(f'Next will scan {scan_range_list[0]}, scan range:\n{scan_range_list[-1]},'
                            f' total points: {len(scan_range_list[-1])}, you can start now')
            self._scan_range_set_flag = 1
            print(self._scan_info)
            logger.info(f'get scan info: {self._scan_info}')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Start_plot_clicked(self):
        """
        check which channel to scan,choose channel by scan info[0] \n
        scan_info=[scan_type,[min_E,min_E+1*step_E...max_E]] \n
        :return:
        """
        # clear all previous scan data
        print(f'start scan process:{self._scan_info}')
        self.clear_all_data()
        print(f'start plot={self._start_plot_flag}-set scan range={self._scan_range_set_flag}')
        if self._start_plot_flag == 0 and self._scan_range_set_flag == 1 and isinstance(self._scan_info,list):
            
            #  scan is off, now scan the channel with the scan_list
            print(f"start scan, Channel:{self._scan_info[0]}")
            self.scan_ch_pA(self._scan_info[0],self._scan_info[-1])
        else:
            # scan is already on, can not start
            print('scan is already on, stop scan or wait!')
            self.raise_info('should set scan range first or scan is already on, stop scan or wait!')

    def set_progress_Bar(self,status:int):
        self.progressBar.setValue(status)
        
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    full sequence of ch-pAmeter scan
    """
    @log_exceptions(log_func=logger.error)
    def scan_ch_pA(self,ch_name,range_list:list):
        """scan one channel and plot
        """
        self._start_plot_flag = 1
        self._scan_ch_flag = 1
        if ch_name and isinstance(range_list, list):
            # set up time hint
            EP_Time = len(range_list) * 6.0
            t_done = time.time() + EP_Time
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Expect_FN_T.setText(f'finishT:{tdone_stamp}')
            self._scan_list = range_list
            self._scan_list_num = len(range_list)
            self._scan_N = 0
            self.scan_start_sig.connect(self.start_ch_pA_set)
            self.scan_start_sig.emit(['OK', self._scan_N])
    
    @log_exceptions(log_func=logger.error)
    @Slot(list)
    def start_ch_pA_set(self, cmd: list):
        if cmd[0] == 'OK':
            # set ch position
            #self.pmc_motor.set_pos(str(self.scan_ch_num),self._scan_list[self._scan_N])
            new_pos=self._scan_list[self._scan_N]
            self.ch_scan_thread = PVmotorThread(self.scan_ch_PVset, new_pos, self.scan_ch_PVrbv, self.ch_PVmovn, 1)
            self.ch_scan_thread.done_signal.connect(self.ch_scan_set_done)
            self.ch_scan_thread.start()

    @log_exceptions(log_func=logger.error)
    @Slot(list)
    def ch_scan_set_done(self, resp: list):
        print(f'get channel {self.scan_channel_name} with set info:{resp}')
        # save the real read-back value for plot
        self._plot_ch_list.append(resp[0])
        # start read pAmeter
        self.ch_pAmeter6485 = Keithley6485Com(port=self.serial_port, func='currents', points=5,full_time=100,keep_on=0)
        self.ch_pAmeter6485.data_sig.connect(self.get_ch_pA_data)
        self.ch_pAmeter6514.start()
    
    @log_exceptions(log_func=logger.error)
    @Slot(list)
    def get_ch_pA_data(self, data: list):
        print(f'get data: {data}')
        if isinstance(data, list):
            current = data[0]
            self._scan_N += 1
            self._plot_pAmeter_list.append(current)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self._time_stamp.append(timestamp)
            # plot scan data
            self.plot_scan_data(self._plot_ch_list, self._plot_pAmeter_list, f'{self.scan_channel_name}', 'Currents(A)')
            if self._scan_N < self._scan_list_num:
                self.scan_start_sig.emit(['OK', self._scan_N])
                self.set_progress_Bar(int(100*self._scan_N/self._scan_list_num))
            else:
                print('all position in list have been set')
                full_data =self.get_full_data()
                t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
                self._save_N += 1
                filename = f'{self.scan_channel_name}_scan_data_{t_stamp}_{self._save_N}'
                folder = time.strftime('%Y-%m-%d', time.localtime())
                save_folder = creatPath(os.path.join(save_path, folder))
                self.save_scan_data(full_data, save_folder, filename)
                # show done time
                self.set_progress_Bar(100)
                done_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Done_time.setText(f'Finished at:{done_stamp}')
                self.scan_start_sig.disconnect(self.start_ch_pA_set)
                self._scan_ch_flag = 0
                self._start_plot_flag = 0


    """
        end full sequence of ch-pA scan
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    plot and data save part
    """

    def plot_scan_data(self, x_list: list, y_list: list, x_name: str, y_name: str):
        """
        plot any x_list and y_list data,and set the Axis name x_name,y_name
        :param x_list:
        :param y_list:
        :param x_name:
        :param y_name:
        :return:
        """
        # plot
        self.figure.axes.cla()
        self.figure.axes.plot(x_list, y_list, marker='o', markersize=3, markerfacecolor='orchid',
                              markeredgecolor='orchid', linestyle='-', color='c')
        self.figure.axes.set_xlabel(x_name, fontsize=18, color='#20B2AA')
        self.figure.axes.set_ylabel(y_name, fontsize=18, color='#20B2AA')
        self.figure.draw()

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    # """
    # data save part
    # """

    def get_full_data(self):
        """
        get the full scan data and return
        :return: full valid scan data(not empty) in dict form
        """
        valid_full_data = dict()
        ch_name=self.scan_channel_name
        temp_full_data = {ch_name: self._plot_ch_list,  'current(pA)': self._plot_pAmeter_list,
                          'time_stamp': self._time_stamp, 'scan set': self._scan_list[0:len(self._plot_ch_list)]}
        # get the valid scan data (not empty)
        for key, value in temp_full_data.items():
            if value:
                valid_full_data[key] = value
        return valid_full_data

    
    # clear all data
    @log_exceptions(log_func=logger.error)
    def clear_all_data(self):
        """
        clear all previous scan data
        :return:
        """
        ch_name=self.scan_channel_name
        temp_full_data = {ch_name: self._plot_ch_list,  'current(pA)': self._plot_pAmeter_list,
                          'time_stamp': self._time_stamp, 'scan set': self._scan_list}
        
        self._plot_ch_list = []
        self._plot_pAmeter_list = []
        self._scan_list = []
        self._time_stamp = []
        self._scan_N = 0

    # save scan data
    def save_scan_data(self, full_data: dict, path, filename):
        """
        save the full data into several file form [dict] form
        :param filename: filename without extension
        :param path: filepath
        :param full_data: {'counts':[list],'Energy':[list]....}
        :return:
        """
        if full_data and os.path.isdir(path):
            #dict_to_csv(full_data, path, filename + '.csv')
            dict_to_excel(full_data, path, filename + '.xlsx')
            #dict_to_json(full_data, path, filename + '.json')
            dict_to_SQLTable(full_data,filename, SQLiteDB_path, 'ALLScanData.db')
            QMessageBox.information(self, 'save file', f'full data have been saved to {path}', QMessageBox.Yes)

    def usr_save_full_data(self, full_data: dict, path: str, usrname='usr_test', usr_define: int = 1):
        """
        check all the data acquired now,save all valid data
        :param usrname: usr defined filename
        :param path: filepath
        :param filename: filename without extension
        :param usr_define: usr define save path and filename->1=yes,0=no
        :return:
        """
        t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
        self._save_N += 1
        filename = usrname + t_stamp + str(self._save_N)
        usr_path = path if os.path.isdir(path) else save_path
        print(filename, usr_path)
        # save scan data
        if full_data:
            if usr_define == 1:
                file_in_path, filetype = QFileDialog.getSaveFileName(self, 'save file', usr_path, 'xlsx(*.xlsx)')
                usr_path = os.path.dirname(file_in_path)
                usr_file = os.path.basename(file_in_path)
                filename = usr_file.split('.')[0]
            self.save_scan_data(full_data, usr_path, filename)
        else:
            if usr_define == 1:
                self.raise_info(f'No data to save')
            else:
                pass

    # # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    # """
    # stop clear data set
    # """

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Stop_plot_clicked(self):
        """
        stop scan disconnect start_scan signal
        :return:
        """
        try:
            if self._start_plot_flag == 0:
                self.raise_info('nothing to stop')
            if self._scan_ch_flag == 1:
                self.scan_start_sig.disconnect(self.start_ch_pA_set)
                self._scan_ch_flag = 0
        except Exception as e:
            print(e)
            logger.error(traceback.format_exc() + str(e))
        else:
            # the scan process has stopped
            self._start_plot_flag = 0
            # save data
            scan_data = self.get_full_data()
            folder = time.strftime('%Y-%m-%d', time.localtime())
            save_folder = creatPath(os.path.join(save_path, folder))
            self.usr_save_full_data(scan_data, path=save_folder, usr_define=1)
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Clear_Save_clicked(self):
        """
        check if any scan is running, if not ,save data then clear all data
        :return:
        """
         
        if self._scan_ch_flag == 0:
            # clear figure
            self.figure.axes.cla()
            self.figure.draw()
            # save data
            scan_data = self.get_full_data()
            self.usr_save_full_data(scan_data, save_path, usr_define=1)
            self.clear_all_data()
        else:
            self.raise_warning('scan is on, can not clear')

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    def closeEvent(self, event):
        if self._start_plot_flag == 1:
            self.raise_info('Stop the scan process before exit!')
            event.ignore()
        elif self._start_plot_flag == 0:
            close = QMessageBox.question(self,
                                                   "QUIT",
                                                   "Are you sure to exit?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QMessageBox.Yes:
                # save data
                # self.usr_save_full_data(usr_define=0)
                self.clear_all_data()
                event.accept()
            else:
                event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BeamMotionPlot()
    win.show()
    sys.exit(app.exec())
