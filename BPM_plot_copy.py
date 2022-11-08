from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
import time, random, sys, os, math, datetime, traceback
# change to Qt6 for python PySide6 and Python310--start_date 2022/07/06
import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout
from PySide6.QtCore import QTimer, Slot, QThread, Signal, Qt,QSize
from PySide6.QtGui import QDoubleValidator, QIntValidator, QTextCursor,QAction,QIcon
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
import pandas as pd

# import main UI function
from UI.UI_BPM_plot import Ui_MainWindow
# import sub UI files
# import my message box
from UI.QtforPython_useful_tools import MyMsgBox, EmittingStr
# import scan range UI
from UI.Input_scan_range import InputScanRange, calculate_scan_range
# import data view plot UI
from UI.Data_View_Plot import DataViewPlot
from UI.SQLDataViewPlot import ViewSQLiteData

# import mcculw lib for DAQ E_1608
from mcculw import ul
from mcculw.enums import ULRange, InterfaceType
from mcculw.ul import ULError, get_net_device_descriptor, create_daq_device
from mcculw.device_info import DaqDeviceInfo
# from pymeasure.adapters.telnet import TelnetAdapter

# import my own matplotlib InitialPlot
from Dependant.My_Matplotlib_PySide6 import Myplot, InitialPlot, NavigationToolbar, MonitorPlot
# import my tool functions for usage
from Dependant.Tools_functions import get_datetime, my_logger, creatPath, to_log, log_exception, log_exceptions, \
    deco_count_time
# import data form to save dict data
from Dependant.Dict_DataFrame_Sqlite import dict_to_excel, dict_to_csv, dict_to_json,dict_to_SQLTable

# import read thread for pAmeter 6517B
#from Linkage.Keithley_pAmeter_driver import Read6517bCurrent
from Linkage.Keithley_pA6517B_driver import Keithley6517BCom
# import BPM control thread
from Linkage.Beam_Position_Motor_control import SetBPMThread
# import DAQ E-1608 read thread
from Linkage.Driver_DAQ_E1608 import search_adc_device, E1608QThread
# import PV_names for Beam position control (dict data form)
from Linkage.EPICS_PV_names import BPM_X, BPM_Z
from numpy import save

# set up the host and port of the ethernet device for E-1608
# PD_host = '169.254.111.100'
ADC_host = '10.30.95.167'
ADC_port = 54211
# ignore instacal Prevents the Universal Library from automatically adding a DAQ device that has been stored
#     in the cb.cfg file by InstaCal
ul.ignore_instacal()
board_num = 0
# pAmeter RS485_To_ethernet address
HOST = '10.30.95.170'
Port_list = [23, 26, 29, 32]  # port in USR_N540
pA_address = (HOST, Port_list[1])
# pA_PORT=TelnetAdapter(HOST,Port_list[1]) # for connection via USR450_To_RS232/485
pA_PORT = 'ASRL6::INSTR'  # for direct connection via RS232/485

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


class BPMMotionPlot(QMainWindow, Ui_MainWindow):
    # signal used
    scan_info_sig = Signal(dict)
    scan_start_sig = Signal(list)

    def __init__(self, parent=None):
        super(BPMMotionPlot, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' BPM motion and PD plot')
        self.__ini_output()
        self.__init_plot__()
        self.__ini_adc__()
        self.__ini_pAmeter__()
        self.__ini_BPM_Motion_()
        self.__ini_BPM_plot__()
        self.__ini_menu_instrument()
        self._ini_menu()

    def __ini_menu_instrument(self):
        self.actionPD_ADC.triggered.connect(self.show_adc_status)
        self.actionpAmeter.triggered.connect(self.show_pAmeter_status)

    @log_exceptions(log_func=logger.error)
    def show_adc_status(self):
        adc_device = search_adc_device(host=self._adc_host, port=ADC_port)
        adc_status = ' connected' if adc_device else ' not found'
        self.msg_box = MyMsgBox(title='ADC status', text=f'{self.Select_ADC.currentText()}' + adc_status,
                                details=f'{self.Select_ADC.currentText()} 'f'in {self._adc_host}:{ADC_port} '
                                        f'{adc_status}\n' + str(adc_device))
        self.msg_box.show()

    def show_pAmeter_status(self, check):
        timeout = 1
        print(f'try connect pAmeter in {timeout}s...')
        pAmeter_status = ''
        current=0
        pA_info = f'pAmeter:keithley6517B\nhost: {HOST}\nPort_2:{Port_list[1]}'
        try:
            #self.pA_PORT = TelnetAdapter(HOST, Port_list[1], timeout=1)
            current=self.ini_keithley6517B_curr(nplc=1,points=5)
        except Exception as e:
            print(e)
            error_info = traceback.format_exc() + str(e) + '\n'
            logger.error(error_info)
            pAmeter_status = f' Not connected with timeout:{timeout}s'
        else:
            pAmeter_status = ' connected'
            self._pAmeter_started = True
        self.msg_box = MyMsgBox(title='pAmeter status', text=f'pAmeter' + pAmeter_status+f'\nget currents:{current:.4f}pA', details=pA_info)
        self.msg_box.show()


    def ini_keithley6517B_curr(self,nplc=5,points=10):
        print('Start setting Keithley6517B....')
        t_start=time.time()
        Keithley6517B = Keithley6517BCom(address=(HOST, Port_list[1]), func='currents', points=points,nplc=nplc)
        ID = Keithley6517B.deviceID
        version = Keithley6517B.version
        print(f'get ID: {ID}\n version:{version}')
        #Keithley6517B.reset()
        Keithley6517B.clear_status()  # 1s
        Keithley6517B.configure_current() # 0.3s
        Keithley6517B.current_filter() # 1.2s
        Keithley6517B.initiate_continuous(continu=True) # 0.1s
        Keithley6517B.current_nplc(nplc=nplc) #1.0s
        Keithley6517B.curr_aver_counts(num=points) #0.1s
        Keithley6517B.zero_check(status='OFF') # 0.1s
        time.sleep(1+nplc/2) # 2s
        resp = Keithley6517B.fresh_data(wait=200) # 0.2s
        data = Keithley6517B.get_value(resp)*1e12
        print(f'set pAmeter done in {(time.time() - t_start):.2f} seconds ')
        return data
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    MenuBar part
    """

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

    def __init__Icons(self):
        """Initial all icons in the menuBar"""
        #icon_path=os.path.join(os.getcwd(),'icons')
        icon_path=os.path.realpath('icons')
        print(f'icon_path: %s' % icon_path)
        data_icon=QIcon(os.path.join(icon_path, 'databricks.svg'))
        database_icon=QIcon(os.path.join(icon_path, 'datacamp.svg'))
        PD_ADC_icon=QIcon(os.path.join(icon_path, 'pkgsrc.svg'))
        pAmeter_icon=QIcon(os.path.join(icon_path, 'avast.svg'))
        self.actionView_data.setIcon(data_icon)
        self.actionDatabase.setIcon(database_icon)
        self.actionPD_ADC.setIcon(PD_ADC_icon)
        self.actionpAmeter.setIcon(pAmeter_icon)
        Eline_icon=QIcon(os.path.join(icon_path, 'databricks.svg')) #databricks
        #Eline_icon=QIcon(os.path.join(icon_path, 'Eline20U_icons.svg'))
        self.setWindowIcon(Eline_icon)
        self.setIconSize(QSize(80,80))

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
        start_info = f'Bean position plot program \n\tby Limin Zhou @SSRF_20U' \
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
    def __init_plot__(self):
        # select instruments
        self.Choose_PD_or_pA.currentIndexChanged['int'].connect(self.choose_PD_pA)
        # self.Choose_PD_or_pA.currentIndexChanged['int'].connect(self.Select_instruments.setCurrentIndex)
        # initialize BPM figure Myplot for usage
        self.figure = InitialPlot()
        # add NavigationToolbar in the figure (widgets)
        self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Plot_box)
        self.gridlayout.addWidget(self.figure)
        self.gridlayout.addWidget(self.fig_ntb)

        # initialize PD Monitor figure Myplot for pAmeter electrometer 6517B usage
        self.PD_pAmeter_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.PD_plot_pAmeter)
        self.gridlayout.addWidget(self.PD_pAmeter_figure)

        # initialize PD Monitor figure Myplot for adc converter usage
        self.PD_ADC_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.PD_plot_adc)
        self.gridlayout.addWidget(self.PD_ADC_figure)

        # initialize BPM X position Monitor figure Myplot for usage
        self.X_pos_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.X_position)
        self.gridlayout.addWidget(self.X_pos_figure)

        # initialize BPM Z position Monitor figure Myplot for usage
        self.Z_pos_figure = MonitorPlot()
        # add NavigationToolbar in the figure (widgets)
        # self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Z_position)
        self.gridlayout.addWidget(self.Z_pos_figure)
        # self.gridlayout.addWidget(self.fig_ntb)

    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def choose_PD_pA(self, n: int):
        """
        choose instrument to measure current
        :return:
        """
        self.Select_instruments.setCurrentIndex(n)
        self.Select_instruments.setTabEnabled((n + 1) % 2, False)
        self.Select_instruments.setTabEnabled(n % 2, True)

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of PD set part
    """

    def __ini_adc__(self):
        self._adc_host = '10.30.95.163'
        self._channel = 0
        self._volt_n = 3
        # select the desired channel and volt_range
        self.ADC_channel.setCurrentIndex(1)
        self.Select_ADC.setCurrentIndex(1)
        self.ADC_ULrange.setCurrentIndex(3)
        self._channel = self.ADC_channel.currentIndex()
        self._volt_n = self.ADC_ULrange.currentIndex()
        self.ADC_channel.currentIndexChanged.connect(self.select_channel)
        self.ADC_ULrange.currentIndexChanged.connect(self.select_volts)
        self.Select_ADC.currentIndexChanged.connect(self.select_adc)
        # set read options
        self._adc_repeat_n = 10
        self._adc_delay = 0.1  # 0.1s
        # set parameters
        self._start_time = time.time()
        # monitor data
        self._MT_delay = []
        self._MT_read = []
        self._monitor_flag = 0

    def select_adc(self):
        """
        select which ADC to use
        0:Ion-adc host=10.30.95.167
        1:RXES-adc host=10.30.95.163
        2:QREXS-adc host=10.30.95.164
        :return:
        """
        adc_n = self.Select_ADC.currentIndex()
        host_list = ['10.30.95.167', '10.30.95.163', '10.30.95.164']
        self._adc_host = host_list[adc_n]
        print(f'select {self.Select_ADC.currentText()} with address: {self._adc_host}:54211')

    def select_channel(self):
        """
        8 channels
        0-7:CH[0-3]L or CH[0-3]H
        :return
        """
        ch_n = self.ADC_channel.currentIndex()
        print(f'channel num: {ch_n}')
        self._channel = self.ADC_channel.currentIndex()
        print(f'Channel:{ch_n} selected')
        print(self._channel)

    def select_volts(self):
        """
        4 voltages
        0:-1V~1V,1:-2V~2V,2:-5V~5V,3:-10V~10V,
        :return
        """
        self._volt_n = self.ADC_ULrange.currentIndex()

        if self._volt_n == 0:
            self._volt_type = ULRange.BIP1VOLTS
        elif self._volt_n == 1:
            self._volt_type = ULRange.BIP2VOLTS
        elif self._volt_n == 2:
            self._volt_type = ULRange.BIP5VOLTS
        elif self._volt_n == 3:
            self._volt_type = ULRange.BIP10VOLTS
        print(f'select UL range:{self._volt_type},current index:{self._volt_n}')

    # @deco_count_time
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Monitor_PD_adc_clicked(self):
        """
        start monitor PD by read from adc
        :return:
        """
        if self._monitor_flag == 0:
            self._MT_delay = []
            self._MT_read = []
            self._start_time = time.time()
            keep_on = 1
            repeat_n = 3
            time_interval = 0.2
            print('start monitoring adc PD')
            try:
                self.PDmonitor_Qthread = E1608QThread(self._channel, self._volt_n, repeat_n, time_interval, keep_on,
                                                      host=self._adc_host, port=ADC_port)
                self.PDmonitor_Qthread.data_sig.connect(self.get_PDmonitor_data)
            except Exception as e:
                print(e)
                error_info = traceback.format_exc() + str(e) + '\n'
                logger.error(error_info)
            else:
                self._monitor_flag = 1
                self.PDmonitor_Qthread.start()
        else:
            QMessageBox.information(self, 'warning', 'Already monitoring', QMessageBox.Yes)

    @Slot(list)
    def get_PDmonitor_data(self, resp: list):
        if resp:
            print(f'received data :{resp}')
            adc_reads = resp[-1]
            # set lcd read
            self.lcd_PD_adc.display(resp[-1])
            self._MT_delay.append(time.time() - self._start_time)
            self._MT_read.append(resp[-1])
            # plot the data [value,delays]
            plot_delay = self._MT_delay
            plot_read = self._MT_read
            if len(self._MT_read) > 200:
                plot_delay = self._MT_delay[-200:]
                plot_read = self._MT_read[-200:]
            # plot
            self.PD_ADC_figure.axes.cla()
            self.PD_ADC_figure.axes.plot(plot_delay, plot_read, '-oc', markersize=1)
            self.PD_ADC_figure.axes.set_title("Read A/D input channel", fontsize=24, color='m')
            self.PD_ADC_figure.axes.set_xlabel("Delay(s)", fontsize=24, color='m')
            self.PD_ADC_figure.axes.set_ylabel("voltage value", fontsize=24, color='m')
            self.PD_ADC_figure.draw()

    @Slot()
    def on_Stop_Monitor_PD_adc_clicked(self):
        # stop the thread
        if self._monitor_flag == 1:
            print('stop monitor')
            self.PDmonitor_Qthread.data_sig.disconnect(self.get_PDmonitor_data)
            self.PDmonitor_Qthread.__del__()
            self._monitor_flag = 0
        else:
            QMessageBox.information(self, 'warning', 'Already stopped', QMessageBox.Yes)

    @Slot()
    def on_Clear_Monitor_PD_adc_clicked(self):
        # clear all the data
        self._MT_delay = []
        self._MT_read = []
        self.PD_ADC_figure.axes.cla()
        self.PD_ADC_figure.draw()
        if self._monitor_flag == 1:
            self.PDmonitor_Qthread.data_sig.disconnect(self.get_PDmonitor_data)
            self.PDmonitor_Qthread.__del__()
        else:
            pass

    """
    end of the PD_ADC part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the PD_pA electrometer part
    """

    def __ini_pAmeter__(self):
        self._MT_pA_currents = []
        self._MT_pA_delay = []
        self._pA_monitor_flag = 0
        self._pA_start_t = 0
        self._MT_save_N=0
        self._pAmeter_started=False

    # @deco_count_time
   # @log_exceptions(log_func=logger.error)
    # @Slot()
    # def on_Monitor_PD_pA_clicked(self):
    #     if self._pA_monitor_flag == 0:
    #         print('Start monitoring pAmeter,timeout=2s')
    #         self._pA_start_t = time.time()
    #         try:
    #             self.pA_PORT = TelnetAdapter(HOST, Port_list[1])
    #         except Exception as e:
    #             print(e)
    #             error_info = traceback.format_exc() + str(e) + '\n'
    #             logger.error(error_info)
    #         else:
    #             self._pA_monitor_flag = 1
    #             self.PD_pAmonitor = Read6517bCurrent(self.pA_PORT, 1, 0.0, 10000, 1)
    #             self.PD_pAmonitor.data_sig.connect(self.get_pAmonitor_data)
    #             self.PD_pAmonitor.start()
    #     else:
    #         self.raise_warning('already monitoring')


    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Monitor_PD_pA_clicked(self):
        if self._pA_monitor_flag == 0:
            print('Start monitoring pAmeter')
            self._pA_start_t = time.time()
            try:
                # initialize keithley 6517b for current measurement
                if not self._pAmeter_started:
                    self.ini_keithley6517B_curr(nplc=5,points=10)
            except Exception as e:
                print(e)
            else:
                self._pA_monitor_flag = 1
                self._pAmeter_started=True
                self._pAmonitor = Keithley6517BCom(address=(HOST, Port_list[1]), func='currents', points=5,
                                                     full_time=600,keep_on=1)
                self._pAmonitor.data_sig.connect(self.get_pAmonitor_data)
                self._pAmonitor.start()
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
            self.lcd_PD_pA.display(resp[0] * 1.0e12)
            self._MT_pA_currents.append(resp[0] * 1.0e12)
            self._MT_pA_delay.append(time.time() - self._pA_start_t)
            # plot the data [value,delays]
            plot_delay = self._MT_pA_delay
            plot_read = self._MT_pA_currents
            if len(self._MT_pA_currents) > 200:
                plot_delay = self._MT_pA_delay[-200:]
                plot_read = self._MT_pA_currents[-200:]
            # plot
            self.PD_pAmeter_figure.axes.cla()
            self.PD_pAmeter_figure.axes.plot(plot_delay, plot_read, '-oc', markersize=1)
            self.PD_pAmeter_figure.axes.set_title("pAmeter read", fontsize=10, color='m')
            self.PD_pAmeter_figure.axes.set_xlabel("Delay(s)", fontsize=10, color='m')
            self.PD_pAmeter_figure.axes.set_ylabel("currents value", fontsize=10, color='m')
            self.PD_pAmeter_figure.draw()

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Stop_Monitor_PD_pA_clicked(self):
        if self._pA_monitor_flag == 1:
            print('stop monitor pAmeter')
            self._pAmonitor.data_sig.disconnect(self.get_pAmonitor_data)
            self._pAmonitor.__del__()
            self._pA_monitor_flag = 0
            # save monitor data
            full_data = {'pA_delay': self._MT_pA_delay, 'current(pA)': self._MT_pA_currents
                         }
            t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
            self._MT_save_N += 1
            filename = f'MT_pA_data_{t_stamp}_{self._save_N}'
            folder = time.strftime('%Y-%m-%d', time.localtime())
            save_folder = creatPath(os.path.join(MT_save_path, folder))
            self.save_scan_data(full_data, save_folder, filename)
        else:
            self.raise_info('not monitoring')

    @Slot()
    def on_Clear_Monitor_PD_clear_clicked(self):
        self._MT_pA_delay = []
        self._MT_pA_currents = []
        self._pA_start_t = 0
        self.PD_pAmeter_figure.axes.cla()
        self.PD_pAmeter_figure.draw()
        if self._pA_monitor_flag == 1:
            self.PD_pAmonitor.data_sig.disconnect(self.get_pAmonitor_data)
            self.PD_pAmonitor.__del__()
            self._pA_monitor_flag = 0
        else:
            pass

    """
    end of the pAmeter part
    """

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the BPM X/Z motor part
    """

    def __ini_BPM_Motion_(self):
        # X  save position and times of change
        self.PV_X_set = BPM_X.get('BPM_X_SET')
        self.PV_X_RBV = BPM_X.get('BPM_X_RBV')
        self.PV_X_MVN = BPM_X.get('BPM_X_SET_MOVN')
        self._pv_X_axis = ''
        self._X_pos = []
        self._X_change_list = []
        self._X_on_num = 0
        self._pv_X_pos = ''
        self._pv_X_set = ''
        self._X_cur_value = ''
        self._step_XL_flag = 0
        self._step_XR_flag = 0
        # Z save position and times of change
        self.PV_Z_set = BPM_Z.get('BPM_Z_SET')
        self.PV_Z_RBV = BPM_Z.get('BPM_Z_RBV')
        self.PV_Z_MVN = BPM_Z.get('BPM_Z_SET_MOVN')
        self._pv_Z_axis = ''
        self._Z_pos = []
        self._Z_change_list = []
        self._Z_on_num = 0
        self._pv_Z_pos = ''
        self._pv_Z_set = ''
        self._Z_cur_value = ''
        self._step_ZL_flag = 0
        self._step_ZR_flag = 0
        # connection to change
        self._step_X_size = 1.0
        self._step_Z_size = 1.0
        self.Step_X_pos.valueChanged.connect(self.get_X_step)
        self.Step_Z_pos.valueChanged.connect(self.get_Z_step)

    @Slot()
    def on_Start_axis_monitor_clicked(self):
        print('start monitoring BPM-X and BPM-Z position')
        self.monitor_X_pos()
        self.monitor_Z_pos()

    # monitor BPM X position
    def monitor_X_pos(self):
        self.PV_X_set = BPM_X.get('BPM_X_SET')
        self.PV_X_RBV = BPM_X.get('BPM_X_RBV')
        self.PV_X_MVN = BPM_X.get('BPM_X_SET_MOVN')
        print(self.PV_X_RBV)
        self._pv_X_axis = PV(self.PV_X_RBV, callback=self.X_pos_changes)
        self._pv_X_set = PV(self.PV_X_set, callback=self.X_set_changes)
        try:
            if self._pv_X_set.connect(timeout=5):
                value = self._pv_X_set.get()
                print(f'connected to BPM X axis,position now: {value}')
                logger.info(f'connected to BPM X axis,position now: {value}')
                if value:
                    self._X_cur_value = float(value)
                    self._X_pos.append(value)
                    self._X_on_num += 1
                    self._X_change_list.append(self._X_on_num)
            else:
                print(f'could not connect to BPM control set:{self._pv_X_set}')
                logger.error(f'could not connect to BPM control set:{self._pv_X_set}')
        except Exception as e:
            print(e)
        finally:
            print('end BPM-X monitor set')

    def X_pos_changes(self, pvname=None, value=None, **kw):
        """
        read back of BPM-X position,record and plot
        :param pvname:
        :param value:
        :param kw:
        :return:
        """
        # print(f'BPM-X motor:{pvname} New Value: {value}  keyword:{kw}\n')
        if value:
            new_value = float(value)
            # self.lcd_X_pos.display(new_value)
            self._X_pos.append(new_value)
            self._X_on_num += 1
            self._X_change_list.append(self._X_on_num)
            # plot the data
            # print("start plot")
            self.plot_X_pos(self._X_change_list, self._X_pos)

    def X_set_changes(self, pvname=None, value=None, **kw):
        """
        get X_axis_set value and display
        :param pvname:
        :param value:
        :param kw:
        :return:
        """
        # print(f'BPM-X position set:{pvname} New Value: {value}  keyword:{kw}\n')
        if value:
            new_value = float(value)
            self._X_cur_value = new_value
            self.lcd_X_pos.display(new_value)

    def plot_X_pos(self, x_num_list, x_pos):
        """
        plot BPM-X position based on list: [x_pos] and change list [x_num_list]
        :param x_pos:
        :param x_num_list:
        :return:
        """
        if x_pos and x_num_list:
            if len(x_pos) > 100:
                x_pos = x_pos[-100:]
                x_num_list = x_num_list[-100:]
            # print(x_pos, x_num_list)
            self.X_pos_figure.axes.cla()
            self.X_pos_figure.axes.plot(x_num_list, x_pos, '-oc', markersize=1)
            self.X_pos_figure.draw()

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # monitor BPM Z position
    def monitor_Z_pos(self):
        self._pv_Z_axis = PV(self.PV_Z_RBV, callback=self.Z_pos_changes)
        self._pv_Z_set = PV(self.PV_Z_set, callback=self.Z_set_changes)
        try:
            connection = self._pv_Z_set.connect()
            if self._pv_Z_set.connect(timeout=5):
                value = self._pv_Z_set.get()
                print(f'connected to BPM Z axis,position now: {value}')
                logger.info(f'connected to BPM Z axis,position now: {value}')
                if value:
                    self._Z_cur_value = float(value)
                    self.lcd_Z_pos.display(float(value))
                    self._Z_pos.append(value)
                    self._Z_on_num += 1
                    self._Z_change_list.append(self._Z_on_num)
            else:
                print(f'could not connect to PGM energy set:{self.PV_Z_set}')
                logger.error(f'could not connect to PGM energy set:{self.PV_Z_set}')
        except Exception as e:
            print(traceback.format_exc() + str(e))
            logger.error(e)
        finally:
            print('end BPM Z monitor set')

    def Z_pos_changes(self, pvname=None, value=None, **kw):
        """
        read back for BPM-Z position,save and plot
        :param pvname:
        :param value:
        :param kw:
        :return:
        """
        # print(f'BPM-Z set:{pvname} New Value: {value}  keyword:{kw}\n')
        if value:
            new_value = float(value)
            self._Z_pos.append(new_value)
            self._Z_on_num += 1
            self._Z_change_list.append(self._Z_on_num)
            # plot the data
            self.plot_Z_pos(self._Z_change_list, self._Z_pos)

    def Z_set_changes(self, pvname=None, value=None, **kw):
        """
        get energy_set value and display
        :param pvname:
        :param value:
        :param kw:
        :return:
        """
        # print(f'BPM-Z pos:{pvname} New Value: {value}  keyword:{kw}\n')
        if value:
            new_value = float(value)
            self._Z_cur_value = new_value
            self.lcd_Z_pos.display(new_value)

    def plot_Z_pos(self, z_pos, z_num_list):
        """
        plot Mirror position based on list: [z_pos] and change list [z_num_list]
        :param z_pos:
        :param z_num_list:
        :return:
        """
        if z_pos and z_num_list:
            if len(z_pos) > 100:
                z_pos = z_pos[-100:]
                z_num_list = z_num_list[-100:]
            self.Z_pos_figure.axes.cla()
            self.Z_pos_figure.axes.plot(z_pos, z_num_list, '-oc', markersize=1)
            self.Z_pos_figure.draw()

    def get_X_step(self):
        """
        get BPM X move step size (um)
        :return:
        """
        self._step_X_size = float(self.Step_X_pos.text().strip(' um'))
        print(f'set BPM X move step size to: {self._step_X_size}')

    def get_Z_step(self):
        """
        get BPM Z move step size (um)
        :return:
        """
        self._step_Z_size = float(self.Step_Z_pos.text().strip(' um'))
        print(f'set BPM Z move step size to :{self._step_Z_size}')

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    Action driver part
    """

    # X axis click step move to set
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_X_pos_right_clicked(self):
        """
        BPM-X move right position X axis ++ forward
        :return:
        """
        if self._step_XL_flag + self._step_XR_flag == 0:
            print(f'right >>step clicked, X axis will forward')
            # check later
            X_current_value = float(self._X_cur_value)
            if X_current_value:
                X_set_value = X_current_value + self._step_X_size
                print(f'BPM Z pos: {X_current_value} move {self._step_X_size}um,++ right is plus')
                logger.info(f'BPM Z pos: {X_current_value} move {self._step_X_size}um,++ right is plus')
                self.set_XstepR_thread = SetBPMThread(self.PV_X_set, X_set_value, self.PV_X_RBV, self.PV_X_MVN, 1)
                self.set_XstepR_thread.done_signal.connect(self.get_stepX_setinfo)
                self.set_XstepR_thread.start()
                self._step_XR_flag = 1
        else:
            self.raise_info('last step not finished , BPM X axis will not move')
            # print(f'last step not finished , BPM X axis will not move')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_X_pos_left_clicked(self):
        """
        BPM-X move left position X axis -- backward
        :return:
        """
        if self._step_XL_flag + self._step_XR_flag == 0:
            print(f'left <<step clicked, BPM X position will backward')
            # check later
            X_current_value = float(self._X_cur_value)
            if X_current_value:
                X_set_value = X_current_value - self._step_X_size
                print(f'BPM X pos: {X_current_value} move {self._step_X_size}um,-- left is minus')
                logger.info(f'BPM X pos: {X_current_value} move {self._step_X_size}um,-- left is minus')
                self.set_XstepL_thread = SetBPMThread(self.PV_X_set, X_set_value, self.PV_X_RBV, self.PV_X_MVN, 1)
                self.set_XstepL_thread.done_signal.connect(self.get_stepX_setinfo)
                self.set_XstepL_thread.start()
                self._step_XL_flag = 1
        else:
            self.raise_info('last step not finished , BPM X will not move')
            # print(f'last step not finished , BPM X axis will not move')

    @Slot(list)
    def get_stepX_setinfo(self, resp: list):
        """
        info = [final_value, self._set_value, self._check_n, self.set_info]
        :param resp:
        :return:
        """
        print(f'get BPM Z set done info\n')
        print(f'final_value: {resp[0]},set_value: {resp[1]},check_N={resp[2]},set_info: {resp[-1]}')
        logger.info(f'final_value: {resp[0]},set_value: {resp[1]},check_N={resp[2]},set_info: {resp[-1]}')
        if self._step_XL_flag == 1:
            self._step_XL_flag = 0
        if self._step_XR_flag == 1:
            self._step_XR_flag = 0

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # BPM Z click step move to set
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Z_pos_right_clicked(self):
        """
        mirror move right position  mirror pos ++ forward
        :return:
        """
        if self._step_ZL_flag + self._step_ZR_flag == 0:
            print(f'right >>step clicked, BPM Z will forward')
            Z_current_value = float(self._Z_cur_value)
            # print(self._Z_cur_value)
            if Z_current_value:
                Z_set_value = Z_current_value + self._step_Z_size
                print(f'BPM Z pos: {Z_current_value} move {self._step_Z_size}um,++ right is plus')
                logger.info(f'BPM Z pos: {Z_current_value} move {self._step_Z_size}um,++ right is plus')
                self.set_ZstepR_thread = SetBPMThread(self.PV_Z_set, Z_set_value, self.PV_Z_RBV, self.PV_Z_MVN, 1)
                self.set_ZstepR_thread.done_signal.connect(self.get_stepZ_setinfo)
                self.set_ZstepR_thread.start()
                self._step_ZR_flag = 1
        else:
            self.raise_info('last step not finished , Energy will not move')
            # print(f'last step not finished , mirror will not move')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Z_pos_left_clicked(self):
        """
        Energy move left position  Energy -- backward
        :return:
        """
        if self._step_ZL_flag + self._step_ZR_flag == 0:
            print(f'left <<step clicked, BPM Z will backward')
            # current value
            Z_current_value = float(self._Z_cur_value)
            if Z_current_value:
                Z_set_value = Z_current_value - self._step_Z_size
                print(f'BPM Z now: {Z_current_value} move {self._step_Z_size}um,-- left is minus')
                logger.info(f'BPM Z now: {Z_current_value} move {self._step_Z_size}um,-- left is minus')
                self.set_ZstepL_thread = SetBPMThread(self.PV_Z_set, Z_set_value, self.PV_Z_RBV, self.PV_Z_MVN, 1)
                self.set_ZstepL_thread.done_signal.connect(self.get_stepZ_setinfo)
                self.set_ZstepL_thread.start()
                self._step_ZL_flag = 1
        else:
            self.raise_info('last step not finished , BPM Z axis will not move')
            # print(f'last step not finished , Z axis will not move')

    @Slot(list)
    def get_stepZ_setinfo(self, resp: list):
        """
        info = [final_value, self._set_value, self._check_n, self.set_info]
        :param resp:
        :return:
        """
        print(f'get BPM Z set done info\n')
        print(f'final_value: {resp[0]},set_value: {resp[1]},check_N={resp[2]},set_info: {resp[-1]}')
        logger.info(f'final_value: {resp[0]},set_value: {resp[1]},check_N={resp[2]},set_info: {resp[-1]}')
        if self._step_ZL_flag == 1:
            self._step_ZL_flag = 0
        if self._step_ZR_flag == 1:
            self._step_ZR_flag = 0

    """
    end of the BPM X/Z step move part 
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the BPM motion vs PD_ADC or pAmeter plot part
    """

    def __ini_BPM_plot__(self):
        # data structure for plot and save
        self._plot_X_list = []
        self._plot_Z_list = []
        self._plot_adc_list = []
        self._plot_pAmeter_list = []
        self._time_stamp = []
        # min-max BPM X/Z axis position and step size (um)
        self._min_X_pos = -100000
        self._max_X_pos = 100000
        self._min_X_step = 0.5
        self._max_X_step = 1000
        self._min_Z_pos = -100000
        self._max_Z_pos = 100000
        self._min_Z_step = 0.5
        self._max_Z_step = 1000
        # flag for status 1 is on , 0 is off
        self._start_plot_flag = 0
        self._scan_range_set_flag = 0
        self._scan_X_adc_flag = 0
        self._scan_X_pA_flag = 0
        self._scan_Z_adc_flag = 0
        self._scan_Z_pA_flag = 0
        # flag for which scan is used 0 is BPM X, 1 is BPM Z
        self._X_or_Z_scan = self.Select_plot_axis.currentIndex()
        self._scan_list = []
        self._scan_list_num = 0  # number of scan list
        self._scan_N = 0  # index of scan list
        self._save_file_flag = 0
        self._save_N = 0  # index for save order

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Input_scan_range_btn_clicked(self):
        """
        check which X axis is chosen(BPM-X or BPM-Z), get the scan range list and return
        :return: scan range list
        """
        self._X_or_Z_scan = self.Select_plot_axis.currentIndex()
        print(f'choose scan X axis {self._X_or_Z_scan}, 0 is X axis,1 is Z axis')
        if self._X_or_Z_scan == 0:
            # X axis using BPM-X
            input_info = f'Input BPM X range:\nmin:{self._min_X_pos}\nmax:{self._max_X_pos}' \
                         f'\nstep range:{self._min_X_step}-{self._max_X_step}'
            self.inputRange_dialog = InputScanRange('BPM-X', input_info)
            self.inputRange_dialog.data_sig.connect(self.get_scan_range)
            self.inputRange_dialog.show()
        elif self._X_or_Z_scan == 1:
            # X axis using BPM-Z
            input_info = f'Input BPM Z range:\nmin:{self._min_Z_pos}\nmax:{self._max_Z_pos}' \
                         f'\nstep range:{self._min_Z_step}-{self._max_Z_step}'
            self.inputRange_dialog = InputScanRange('BPM-Z', input_info)
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
            self.raise_info(f'Next will scan {scan_range_list[0]},scan range:\n{scan_range_list[-1]},'
                            f'total points: {len(scan_range_list[-1])}, you can start now')
            self._scan_range_set_flag = 1
            print(self._scan_info)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Start_plot_clicked(self):
        """
        check which Y axis should choose (PD reader or pAmeter),choose X axis by scan info[0] \n
        scan_info=[scan_type,[min_E,min_E+1*step_E...max_E]] \n
        :return:
        """
        # clear all previous scan data
        self.clear_all_data()
        print(
            f'start plot={self._start_plot_flag}-set scan range={self._scan_range_set_flag},{self.Choose_PD_or_pA.currentIndex()}')
        if self._start_plot_flag == 0 and self._scan_range_set_flag == 1:
            # scan is off
            print(f'scan info={self._scan_info}')
            if self._scan_info[0] == 'BPM-X' and self.Choose_PD_or_pA.currentIndex() == 0:
                # X axis: BPM-X, Y axis: PD reader
                self.scan_X_adc(self._scan_info[-1])
            elif self._scan_info[0] == 'BPM-X' and self.Choose_PD_or_pA.currentIndex() == 1:
                # X axis: BPM-X, Y axis: pA-meter
                self.scan_X_pA(self._scan_info[-1])
            elif self._scan_info[0] == 'BPM-Z' and self.Choose_PD_or_pA.currentIndex() == 0:
                # X axis: BPM-Z, Y axis: PD reader
                self.scan_Z_adc(self._scan_info[-1])
            elif self._scan_info[0] == 'BPM-Z' and self.Choose_PD_or_pA.currentIndex() == 1:
                # X axis: BPM-Z, Y axis: pA-meter
                print("start scan, X axis: BPM-Z, Y axis: pA-meter")
                self.scan_Z_pA(self._scan_info[-1])
        elif self._start_plot_flag == 0 and self._scan_range_set_flag == 0:
            # scan range not set
            self.raise_info('should set scan range first')
        elif self._start_plot_flag == 1:
            # scan is already on, can not start
            self.raise_info('scan is already on, stop scan or wait!')

    def set_progress_Bar(self,status:int):
        self.progressBar.setValue(status)
        
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    full sequence of BPM-X-adc scan
    """

    def scan_X_adc(self, range_list: list):
        self._start_plot_flag = 1
        self._scan_X_adc_flag = 1
        if isinstance(range_list, list):
            # set up time hint
            EP_Time = len(range_list) * 6.0
            t_done = time.time() + EP_Time
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Expect_FN_T.setText(f'Expect to finish at:{tdone_stamp}')
            self._scan_list = range_list
            self._scan_list_num = len(range_list)
            self._scan_N = 0
            self.scan_start_sig.connect(self.start_X_adc_set)
            self.scan_start_sig.emit(['OK', self._scan_N])

    @Slot(list)
    def start_X_adc_set(self, cmd: list):
        if cmd[0] == 'OK':
            self.XsetQThread = SetBPMThread(self.PV_X_set, self._scan_list[self._scan_N], self.PV_X_RBV, self.PV_X_MVN,
                                            1)
            self.XsetQThread.done_signal.connect(self.X_adc_set_done)
            self.XsetQThread.start()

    @Slot(list)
    def X_adc_set_done(self, resp: list):
        print(f'get BPM X axis set info:{resp}')
        # save the real read-back value for plot
        self._plot_X_list.append(resp[0])
        # start read adc voltage
        self.adcReadQthread = E1608QThread(self._channel, self._volt_n, self._adc_repeat_n, self._adc_delay, keep_on=0,
                                           host=self._adc_host, port=ADC_port)
        self.adcReadQthread.data_sig.connect(self.get_X_adc_data)
        self.adcReadQthread.start()

    @Slot(list)
    def get_X_adc_data(self, data: list):
        print(f'get data: {data}')
        if isinstance(data, list):
            voltage = data[-1]
            self._scan_N += 1
            self._plot_adc_list.append(voltage)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self._time_stamp.append(timestamp)
            # plot scan data
            self.plot_scan_data(self._plot_X_list, self._plot_adc_list, 'BPM X axis(um)', 'adc voltage(V)')
            if self._scan_N < self._scan_list_num:
                self.scan_start_sig.emit(['OK', self._scan_N])
                self.set_progress_Bar(int(100*self._scan_N/self._scan_list_num))
            else:
                print('all position in list have been set')
                full_data = {'BPM-X pos': self._plot_X_list, 'adc voltage(V)': self._plot_adc_list,
                             'time stamp': self._time_stamp, 'BPM-X set': self._scan_list}
                t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
                self._save_N += 1
                filename = f'X_adc_data_{t_stamp}_{self._save_N}'
                folder = time.strftime('%Y-%m-%d', time.localtime())
                save_folder = creatPath(os.path.join(save_path, folder))
                self.save_scan_data(full_data, save_folder, filename)
                # show done time
                self.set_progress_Bar(100)
                done_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Done_time.setText(f'Finished at:{done_stamp}')
                self._scan_X_adc_flag = 0
                self._start_plot_flag = 0

    """
    full sequence of BPM-X-adc scan
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    full sequence of BPM-X-pA scan
    """

    def scan_X_pA(self, range_list: list):
        self._start_plot_flag = 1
        self._scan_X_pA_flag = 1
        if isinstance(range_list, list):
            # set up time hint
            EP_Time = len(range_list) * 6.0
            t_done = time.time() + EP_Time
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Expect_FN_T.setText(f'Expect to finish at:{tdone_stamp}')
            self._scan_list = range_list
            self._scan_list_num = len(range_list)
            self._scan_N = 0
            self.scan_start_sig.connect(self.start_X_pA_set)
            self.scan_start_sig.emit(['OK', self._scan_N])

    @Slot(list)
    def start_X_pA_set(self, cmd: list):
        if cmd[0] == 'OK':
            print(cmd)
            new_value = self._scan_list[self._scan_N]
            print(f'new_value: {new_value}')
            self.XpAsetQThread = SetBPMThread(self.PV_X_set, self._scan_list[self._scan_N], self.PV_X_RBV,
                                              self.PV_X_MVN, 1)
            self.XpAsetQThread.done_signal.connect(self.X_set_done)
            self.XpAsetQThread.start()

    @Slot(list)
    def X_set_done(self, resp: list):
        print(f'get BPM-X set info: {resp}')
        self._plot_X_list.append(resp[0])
        # start read adc voltage
        try:
            self.pAX_ReadQthread = Keithley6517BCom(address=(HOST, Port_list[1]), func='currents', points=5,
                                                    full_time=600, keep_on=0)
            self.pAX_ReadQthread.data_sig.connect(self.get_X_pA_data)
            self.pAX_ReadQthread.start()
        except Exception as e:
            print(e)
            error_info = traceback.format_exc() + str(e) + '\n'
            logger.error(error_info)


    @Slot(list)
    def get_X_pA_data(self, data: list):
        if data[-1] == 'OK':
            currents = data[0] * 1.0e12
            self._scan_N += 1
            self._plot_pAmeter_list.append(currents)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self._time_stamp.append(timestamp)
            self.plot_scan_data(self._plot_X_list, self._plot_pAmeter_list, 'BPM X axis(um)', 'current(pA)')
            if self._scan_N < self._scan_list_num:
                self.scan_start_sig.emit(['OK', self._scan_N])
                self.set_progress_Bar(int(100*self._scan_N/self._scan_list_num))
            else:
                print('all position in list have been set')
                full_data = {'BPM-X pos': self._plot_X_list, 'current(pA)': self._plot_pAmeter_list,
                             'time_stamp': self._time_stamp, 'BPM-X set': self._scan_list}
                t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
                self._save_N += 1
                filename = f'X_pA_data_{t_stamp}_{self._save_N}'
                folder = time.strftime('%Y-%m-%d', time.localtime())
                save_folder = creatPath(os.path.join(save_path, folder))
                self.save_scan_data(full_data, save_folder, filename)
                # show done time
                self.set_progress_Bar(100)
                done_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Done_time.setText(f'Finished at:{done_stamp}')
                self._scan_X_pA_flag = 0
                self._start_plot_flag = 0
                self.scan_start_sig.disconnect(self.start_X_pA_set)

    """
    full sequence of BPM-X-pAmeter scan
    """

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
        full sequence of BPM-Z-adc scan
    """

    def scan_Z_adc(self, range_list: list):
        self._start_plot_flag = 1
        self._scan_Z_adc_flag = 1
        if isinstance(range_list, list):
            # set up time hint
            EP_Time = len(range_list) * 6.6
            t_done = time.time() + EP_Time
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Expect_FN_T.setText(f'Due finish at:{tdone_stamp}')
            self._scan_list = range_list
            self._scan_list_num = len(range_list)
            self._scan_N = 0
            self.scan_start_sig.connect(self.start_Z_adc_set)
            self.scan_start_sig.emit(['OK', self._scan_N])

    @Slot(list)
    def start_Z_adc_set(self, cmd: list):
        if cmd[0] == 'OK':
            # print(cmd)
            self.ZsetQThread = SetBPMThread(self.PV_Z_set, self._scan_list[self._scan_N],
                                            self.PV_Z_RBV, self.PV_Z_MVN, 1)
            self.ZsetQThread.done_signal.connect(self.Z_adc_set_done)
            self.ZsetQThread.start()

    @Slot(list)
    def Z_adc_set_done(self, resp: list):
        print(f'get BPM-Z set info:{resp}')
        self._plot_Z_list.append(resp[0])
        # start read adc voltage
        self.adcZReadQthread = E1608QThread(self._channel, self._volt_n, self._adc_repeat_n, self._adc_delay, keep_on=0,
                                            host=self._adc_host, port=ADC_port)
        self.adcZReadQthread.data_sig.connect(self.get_Z_adc_data)
        self.adcZReadQthread.start()

    @Slot(list)
    def get_Z_adc_data(self, data: list):
        print(f'get data: {data}')
        if isinstance(data, list):
            voltage = data[-1]
            self._scan_N += 1
            self._plot_adc_list.append(voltage)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self._time_stamp.append(timestamp)
            self.plot_scan_data(self._plot_Z_list, self._plot_adc_list, 'BPM Z axis(um)', 'adc voltage(V)')
            if self._scan_N < self._scan_list_num:
                self.scan_start_sig.emit(['OK', self._scan_N])
                self.set_progress_Bar(int(100*self._scan_N/self._scan_list_num))
            else:
                print('all position in list have been set')
                full_data = {'BPM-Z pos': self._plot_X_list, 'adc voltage': self._plot_adc_list,
                             'time stamp': self._time_stamp, 'BPM-Z set': self._scan_list}
                t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
                self._save_N += 1
                filename = f'Z_adc_data_{t_stamp}_{self._save_N}'
                folder = time.strftime('%Y-%m-%d', time.localtime())
                save_folder = creatPath(os.path.join(save_path, folder))
                self.save_scan_data(full_data, save_folder, filename)
                # show done time
                self.set_progress_Bar(100)
                done_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Done_time.setText(f'Finished at:{done_stamp}')
                self._scan_Z_adc_flag = 0
                self.scan_start_sig.disconnect(self.start_Z_adc_set)
                self._start_plot_flag = 0

    """
        end full sequence of BPM-Z-adc scan
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
        full sequence of BPM-Z-pA scan
        """

    @log_exceptions(log_func=logger.error)
    def scan_Z_pA(self, range_list: list):
        print('begin BPM-Z pAmeter scan')
        self._start_plot_flag = 1
        self._scan_Z_pA_flag = 1
        if isinstance(range_list, list):
            # set up time hint
            print(range_list)
            EP_Time = len(range_list) * 6.6
            t_done = time.time() + EP_Time
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Expect_FN_T.setText(f'Due finish at:{tdone_stamp}')
            self._scan_list = range_list
            self._scan_list_num = len(range_list)
            self._scan_N = 0
            self.scan_start_sig.connect(self.start_Z_pA_set)
            self.scan_start_sig.emit(['OK', self._scan_N])

    @Slot(list)
    def start_Z_pA_set(self, cmd: list):
        if cmd[0] == 'OK':
            print(cmd)
            new_value = self._scan_list[self._scan_N]
            print(f'new_value: {new_value}')
            self.ZsetQThread = SetBPMThread(self.PV_Z_set, self._scan_list[self._scan_N],
                                            self.PV_Z_RBV, self.PV_Z_MVN, 1)
            self.ZsetQThread.done_signal.connect(self.Z_pA_set_done)
            self.ZsetQThread.start()

    @Slot(list)
    def Z_pA_set_done(self, resp: list):
        print(f'get BPM-Z set info:{resp}')
        self._plot_Z_list.append(resp[0])
        # start reading currents
        self.pAZReadQthread = Keithley6517BCom(address=(HOST, Port_list[1]), func='currents', points=5,
                                                     full_time=600,keep_on=0)
        self.pAZReadQthread.data_sig.connect(self.get_Z_pA_data)
        self.pAZReadQthread.start()

    @Slot(list)
    def get_Z_pA_data(self, data: list):
        print(f'get data: {data}')
        if isinstance(data, list):
            I_pA = data[0] * 1.0e12
            self._scan_N += 1
            self._plot_pAmeter_list.append(I_pA)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self._time_stamp.append(timestamp)
            self.plot_scan_data(self._plot_Z_list, self._plot_pAmeter_list, 'BPM Z axis(um)', 'Current(pA)')
            if self._scan_N < self._scan_list_num:
                self.scan_start_sig.emit(['OK', self._scan_N])
                self.set_progress_Bar(int(100*self._scan_N/self._scan_list_num))
            else:
                print('all position in list have been set')
                full_data = {'BPM-Z pos': self._plot_Z_list, 'pA current(A)': self._plot_pAmeter_list,
                             'time_stamp': self._time_stamp, 'BPM-Z set': self._scan_list}
                t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
                self._save_N += 1
                filename = f'Z_pA_data_{t_stamp}_{self._save_N}'
                folder = time.strftime('%Y-%m-%d', time.localtime())
                save_folder = creatPath(os.path.join(save_path, folder))
                self.save_scan_data(full_data, save_folder, filename)
                # show done time
                self.set_progress_Bar(100)
                done_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Done_time.setText(f'Finished at:{done_stamp}')
                self._scan_Z_pA_flag = 0
                self.scan_start_sig.disconnect(self.start_Z_pA_set)
                self._start_plot_flag = 0

    """
        end full sequence of BPM-Z-pA scan
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
    """
    data save part
    """

    def get_full_data(self):
        """
        get the full scan data and return
        :return: full valid scan data(not empty) in dict form
        """
        valid_full_data = dict()
        temp_full_data = {'BPM-X pos(um)': self._plot_X_list, 'BPM-Z pos(um)': self._plot_Z_list,
                          'adc voltage(V)': self._plot_adc_list, 'current(pA)': self._plot_pAmeter_list,
                          'time_stamp': self._time_stamp, 'scan set': self._scan_list}
        # get the valid scan data (not empty)
        for key, value in temp_full_data.items():
            if value:
                valid_full_data[key] = value
        return valid_full_data

    # clear all data
    def clear_all_data(self):
        """
        clear all previous scan data
        :return:
        """
        full_data = {'BPM-X pos(um)': self._plot_X_list, 'BPM-Z pos(um)': self._plot_Z_list,
                     'adc voltage(V)': self._plot_adc_list, 'current(pA)': self._plot_pAmeter_list,
                     'time_stamp': self._time_stamp, 'scan set': self._scan_list}
        self._plot_X_list = []
        self._plot_Z_list = []
        self._plot_pAmeter_list = []
        self._plot_adc_list = []
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
            dict_to_csv(full_data, path, filename + '.csv')
            dict_to_excel(full_data, path, filename + '.xlsx')
            dict_to_json(full_data, path, filename + '.json')
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

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    stop clear data set
    """

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
            if self._scan_X_adc_flag == 1:
                self.scan_start_sig.disconnect(self.start_X_adc_set)
                self._scan_X_adc_flag = 0
            elif self._scan_X_pA_flag == 1:
                self.scan_start_sig.disconnect(self.start_X_pA_set)
                self._scan_X_pA_flag = 0
            elif self._scan_Z_adc_flag == 1:
                self.scan_start_sig.disconnect(self.start_Z_adc_set)
                self._scan_Z_adc_flag = 0
            elif self._scan_Z_pA_flag == 1:
                self.scan_start_sig.disconnect(self.start_Z_pA_set)
                self._scan_Z_pA_flag = 0
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
        flag_value = self._scan_X_adc_flag + self._scan_X_pA_flag + self._scan_Z_adc_flag + self._scan_Z_pA_flag
        if flag_value == 0:
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
            close = QtWidgets.QMessageBox.question(self,
                                                   "QUIT",
                                                   "Are you sure to exit?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QtWidgets.QMessageBox.Yes:
                # save data
                # self.usr_save_full_data(usr_define=0)
                self.clear_all_data()
                event.accept()
            else:
                event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BPMMotionPlot()
    win.show()
    sys.exit(app.exec())
