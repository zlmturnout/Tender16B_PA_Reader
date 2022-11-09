import logging
import math
import os
import re
import sys
import time
import traceback
from socket import *
from time import sleep

import numpy as np
import pandas as pd
# from Dependant.Tools_functions import my_logger, creatPath
#from SCIP_CMD_6517B import *
import serial
import serial.tools.list_ports
from PySide6.QtCore import QObject, QThread, QTimer, Signal, Slot
from serial import SerialException


def my_logger(log_file: str = 'output.log', logger_name: str = 'usr_test'):
    """
    return a logger for logging
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def creatPath(file_path):
    """
    create a given path if not exist and return it
    :param file_path:
    :return: file_path
    """
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    return file_path


HOST = '10.30.95.170'
Port_list = [23, 26, 29, 32]  # port in USR_N540,26 is for keithley 6517B
BUFSIZ = 1024
log_path = os.path.join(os.getcwd(), 'log_info')
creatPath(log_path)
# logger
log_file = f'Keithley6514_{time.strftime("%Y-%m-%d", time.localtime())}.log'
Keithley6485_logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Keithley6517B')

"""
worker Qthread for reading current[aA~mA] from Keithley 6514 electrometer
"""
# basic logic to measure current by Keithley 6517b
# *CLS (clear status)
cmd_cls = '*CLS'
# reset 6517B
cmd_RST = '*RST'
# zero check status
cmd_zch = ':SYSTem:ZCHeck?'  # 0 is OFF , 1 is ON
# get the version
cmd_version=':SYSTem:VerSion?'

# zero check on
cmd_zch=':SYSTem:ZCHeck?' # 0 is OFF , 1 is ON
cmd_zch_on=':SYSTem:ZCHeck ON'
cmd_zch_off=':SYSTem:ZCHeck OFF'
# local state and remote state
cmd_local=':SYSTem:LOCal'
cmd_remote=':SYSTem:REMote'

# reads the identification code
cmd_ID='*IDN?' # KEITHLEY INSTRUMENTS INC.,MODEL 6517B,4402161,A13/700x

# reset 6517B
cmd_RST='*RST'
cmd_preset=':SYSTem:PRESet' # Return to :SYST:PRES defaults


# configure measure current
cmd_config_CURR = ':CONFigure:CURR:DC'
# set filter type=advance mode=average  counts=5  noise=1% and median OFF
cmd_curr_aver = ':SENS:CURR:AVERage:TCONtrol?'
# initiate continues on
cmd_initiate = ':INITiate'  # take the Model 6517B out of the idle state wait 1s
# return a new value
#cmd_get_newval = ':SENS:DATA:FRESh?'
# data type [re.fullmatch(r'([+\-0-9E.]+)[A-Z]{4}', result[0])]
test_data = '+198.4891E-12A,+2.236299E+02,+1.380000E+02\r\n'

# Signal-oriented measurement commands
cmd_fetch=':FETCH?' #Requests the latest reading
cmd_config_use=':CONFigure:<function>' #CONFigure:CURR:DC

cmd_read='READ?' # Performs an :ABORt, :INITiate, and a :FETCh?
cmd_mea=':MEASure[:<function>]?' #Performs an :ABORt, :CONFigure:<function>, and a :READ?

# configure measure current
cmd_config_CURR=':CONFigure:CURR:DC'
cmd_sens_curr=":SENS:FUNC:'CURR'"
cmd_curr_AutoRange='CURR:RANGe:AUTO '
cmd_curr_RangeSet='CURR:RANGe ' # add [val]:0-21E-3
cmd_curr_nplc=':SENS:CURR:NPLC '# add [val]:0.01-5
cmd_curr_dig='DISP:DIG ' # add [val]:4=3.5,5=4.5, 6=5.5, 7=6.5,



class Keithley6485Com(QThread):
    """
        worker Qthread for communicating with Keithley 6514B electrometer,using serial port
        emit signal current data when complete:[average,all currents,info]
        # function:read currents implemented
        """
    data_sig = Signal(list)

    def __init__(self, port, func: str, points: int = 5, delay: float = 0.1, full_time: float = 1000,
                 keep_on: int = 0, nplc: int = 1,
                 parent=None):
        #QThread.__init__(self, parent)
        super(Keithley6485Com, self).__init__(parent)
        #self.address = address
        self.func = func
        self.points = points
        self.delay = delay
        self.nplc = nplc
        self.monitor_time = full_time  # monitor for 1000s
        self.run_flag = True
        self._keep_on = keep_on
        print(f'keep on =={keep_on}')
        self.response_msg = ''
        #self.serial = serial.Serial()
        #self.serial = serial.Serial(port)
        self.serial = port
        #self.open_port(port)


    def open_port(self, port:str):
        """
        open port for data transmission
        :return:
        """
        status_txt='no info'
        try:
            self.serial.port = port
            self.serial.baudrate = 9600
            self.serial.stopbits = 1
            self.serial.bytesize = 8
            self.serial.parity = 'N'
            self.serial.open()
        except Exception as e:
            print(e)
            status_txt=e
        else:
            status_txt='OK'
        return status_txt

    def close_port(self):
        """
        close the port
        :return: 
        """
        status_txt=None
        if self.serial.isOpen():
            try:
                self.serial.close()
            except Exception as e:
                status_txt=e
            else:
                status_txt='OK'
        return status_txt


    def __del__(self):
        self.run_flag = False
        #self.close_port()

    def set_keep_on(self,keep_on:int):
        """keep on monitoring
        1 is on,0 is off

        Args:
            keep_on (int): _description_
        """
        self._keep_on=keep_on # 0 is off, 1 is on

    def cmd_send_ethernet(self, cmd: str, wait: int = 100, receive_flag=True):
        """
        send cmd to the keithley address, get the response and return
        start tcp client,set up connection to the sever USR_N540,
        send msg and return when get response message
        :param receive_flag: if true receive and return, else wait and return NONE
        :param wait: wait [100]ms before the cmd is write
        :param cmd:
        :return:
        """
        self.send_msg = (cmd + '\r\n').encode('utf-8')
        self.socket_TCP = socket(AF_INET, SOCK_STREAM)
        self.socket_TCP.settimeout(2.0)  # set timeout
        try:
            self.socket_TCP.connect(self.address)
        except Exception as e:
            error_info = traceback.format_exc()
            print(error_info)
            Keithley6485_logger.error("Connection fail %s", e, exc_info=True)
        else:
            self.connect_flag = True
            self.socket_TCP.send(self.send_msg)
            self.msleep(wait)
            t_start = time.time()
            while self.connect_flag and receive_flag and time.time() - t_start < 10:
                resp = self.socket_TCP.recv(BUFSIZ)
                if resp:
                    self.response_msg = resp.decode('utf-8')
                    Keithley6485_logger.info("get response %s", self.response_msg)
                    # print(f'response:{self.response_msg} from address:{self.address}')
                    break
        finally:
            # self.connect_flag = True
            self.socket_TCP.close()
            return self.response_msg

    def cmd_send(self, cmd, read_timeout=2,receive_flag=True,wait: int = 100):
        """
        write cmd via serial port
        :param read_timeout:  read timeout default=5s
        :param cmd: CMD to be send
        :return:
        """
        send_msg = (cmd + '\r\n').encode('utf-8')
        if self.serial.isOpen():
            self.read_flag = True
            rec_data = b''
            try:
                self.serial.write(send_msg)
            except SerialException as e:
                print(e)
            else:
                self.msleep(wait)
                t0 = time.time()
                while self.read_flag and receive_flag and time.time() - t0 < read_timeout:
                    wait_Num = self.serial.in_waiting
                    if wait_Num > 0:
                        rec_data += self.serial.read(wait_Num)
                        # end read when get the stop bit '\n'
                        if b'\r' in rec_data:
                            self.read_flag = False
                            print(f'data reciveied in {1000 * (time.time() - t0):.4f}ms')
            finally:
                return rec_data.decode('utf-8')


    @property
    def deviceID(self):
        deviceID = self.cmd_send(cmd_ID)
        return deviceID

    @property
    def version(self):
        return self.cmd_send(cmd_version)

    def reset(self):
        self.cmd_send(cmd_RST, wait=1000, receive_flag=False)

    def clear_status(self):
        self.cmd_send(cmd_cls, wait=1000, receive_flag=False)

    def zero_check(self, status: str = 'ON'):
        """
        set zero check mode, OFF is off, ON is on
        :param status:
        :return:
        """
        if status == 'ON':
            self.cmd_send(cmd_zch_on, receive_flag=False)
        elif status == 'OFF':
            self.cmd_send(cmd_zch_off, receive_flag=False)

    def configure_current(self, AutoRange: int = 1, Range: float = 0.01, nplc: float = 1, Digits: int = 7):
        """
        :SENS:FUNC:'CURR'
        configure measure current
        :param AutoRange: auto range 0 is off,1 is on
        :param Range: 0-21e-3 A
        :param nplc: 0.01,1,10, fast,median,low
        :param Digits: add [val]:4=3.5,5=4.5, 6=5.5, 7=6.5,
        :return:
        """
        cmd_setRange = ''
        if AutoRange == 1:
            cmd_setRange = cmd_curr_AutoRange + str(AutoRange)
        elif AutoRange == 0:
            cmd_setRange = cmd_curr_AutoRange + str(AutoRange) + ';' + cmd_curr_RangeSet + str(Range)
        cmd = cmd_sens_curr + ';' + cmd_setRange + ';' 
        self.cmd_send(cmd, wait=1000, receive_flag=False)

    def current_nplc(self,nplc:int=5):
        """

        set the nplc for current measurement 0.01,1,10=Fastest,Normal,Slowest
        :param nplc:
        :return:
        """
        cmd=cmd_curr_nplc + str(nplc)
        wait = 1000 if self.nplc == 10 else 2000
        self.cmd_send(cmd, wait=wait, receive_flag=False)

    # def current_filter(self, useFilter=True, FilterType='ADV', AverConTr='REP'):
    #     """
    #     configure the current filter,
    #     :param useFilter: True:ON,False:OFF
    #     :param FilterType: SCALar or ADVanced
    #     :param AverConTr: REPeat or MOVing
    #     :param averCount: average over 1-100
    #     :param Noise: +/- [val]% val:1-100
    #     :param MediaMode: True is On, False is OFF
    #     :return:
    #     """
    #     cmd_filter = cmd_curr_filterON if useFilter else cmd_curr_filterOFF
    #     cmd_FilterType = cmd_curr_aver_typeADV if FilterType == 'ADV' else cmd_curr_aver_typeSCAL
    #     cmd_AverConTr = cmd_curr_averREP if AverConTr == 'REP' else cmd_curr_averMOV
    #     #cmd_curr_aver_noiseToL = cmd_curr_aver_Noise_N + str(Noise)
    #     # write the cmd
    #     self.cmd_send(cmd_filter,wait=500,receive_flag=False)
    #     cmd =cmd_FilterType + ';' + cmd_AverConTr + ';'
    #     print(cmd)
    #     self.cmd_send(cmd, wait=500, receive_flag=False)
    #     # remove filter
    #     self.cmd_send(cmd_curr_filterOFF,wait=200,receive_flag=False)

    # def curr_medianMode(self,MediaMode=False):
    #     """
    #     cmd=SENS:CURRent:median:STATe ON/OFF
    #     medianMode On or OFF
    #     :return:
    #     """
    #     cmd_curr_medianMode = cmd_curr_medianON if MediaMode else cmd_curr_medianOFF
    #     self.cmd_send(cmd_curr_medianMode,wait=200,receive_flag=False)


    def curr_aver_counts(self, num: int = 5):
        """
        cmd=:SENS:CURR:AVERage:Count [num]
        set the average num in filter
        :param num:
        :param counts:
        :return:
        """
        cmd_curr_aver_Num="AVER:COUN "
        cmd = cmd_curr_aver_Num + str(num)
        self.cmd_send(cmd, wait=100, receive_flag=False)

    def initiate(self):
        """
        cmd=:INITiate
        take the Model 6517B out of the idle state
        :return:
        """
        self.cmd_send(cmd_initiate, wait=100, receive_flag=False)

    
    # configure measure function
    def conf_function(self, func='current',wait:int=100):
        """
        function:CURRent[:DC]: Amps function
                RESistance: Ohms function
                CHARge: Coulombs function
                VOLTage[:DC]:default voltage
        :return:
        """
        if func == 'current':
            cmd_conf_func = ':CONFigure:CURRent:DC;'
        elif func == 'resistance':
            cmd_conf_func = ':CONFigure:RESistance;'
        elif func == 'charge':
            cmd_conf_func = ':CONFigure:CHARge;'
        else:
            cmd_conf_func = ':CONFigure:VOLTage:DC;'
        self.cmd_send(cmd_conf_func, wait=wait, receive_flag=False)

    # common cmd for measurement
    # Signal-oriented measurement commands
    def fetch(self, wait: int = 100):
        """
        cmd=:FETCH?
        Requests the latest reading
        :return:
        """
        result = self.cmd_send(cmd_fetch, wait=wait, receive_flag=True)
        return result

    def _MEAs(self, wait: int = 100):
        """
        Performs an :ABORt, :CONFigure:<function>, and a :READ?
        NOT recommended
        :return:
        """
        return self.cmd_send(cmd_mea, wait=wait, receive_flag=True)

    def read_data(self, wait: int = 100):
        """
        Trigger measurement(s) and request reading(s)
        Args:
            wait (int): wait for recieve 100
        :return:
        """
        return self.cmd_send(cmd_read, wait=wait, receive_flag=True)

    @staticmethod
    def get_value(resp: str):
        """
        test_data='+198.4891E-12NADC,+0007633.858813secs,+58454RDNG#\r\n'
        :param resp:
        :return:0 if wrong, else currents  in Amps
        """
        data_value = 0
        if resp:
            print(f'get resp:{resp}')
            # val = re.fullmatch(r'([+\-0-9E.]+)[A-Z]{4}', resp.split(',')[0])
            val = re.fullmatch(r'([+\-0-9E.]+)[A]', resp.split(',')[0])
            data_value = float(val.group(1))
            #val=resp.split(',')[0]
            #data_value = float(str(val[0]))
        print(f'get new read:{data_value}A')
        return data_value

    def run(self):
        print(self.func)
        t0 = time.time()
        status = 'OK'
        pA_currents=0
        # measure current
        if self.func == 'currents':
            #self.zero_check(status='OFF')
            #self.current_nplc(nplc=self.nplc)
            #self.conf_function(self.func,wait=1000)
            #self.msleep(2000)
            #self.curr_aver_counts(num=self.points)
            print("Now monitoring")
            sum_current=0
            average_n=3
            while self.run_flag and time.time() - t0 < self.monitor_time:
                try:
                    # if self._keep_on == 0:
                    #     i=0
                    #     t_start=time.time()
                    #     while i<average_n:
                    #         resp = self.read_data(wait=100)
                    #         data = self.get_value(resp)
                    #         i+=1
                    #         sum_current+=data
                    #     pA_currents=sum_current/average_n
                    # else:
                    #     #self.conf_function('current',wait=100)
                    #     self.msleep(200)
                    #     resp = self.read_data(wait=100)
                    #     #print(f'get resp read:{resp}')
                    #     pA_currents = self.get_value(resp)
                    #     status = 'error' if pA_currents == 0 else 'OK'
                    #self.conf_function('current',wait=100)
                    self.msleep(200)
                    resp = self.read_data(wait=100)
                    #print(f'get resp read:{resp}')
                    pA_currents = self.get_value(resp)
                    status = 'error' if pA_currents == 0 else 'OK'
                except Exception as e:
                    error_info = traceback.format_exc()
                    print(error_info)
                    Keithley6485_logger.error("Connection fail %s", e, exc_info=True)
                finally:
                    print(f'start emit:{[pA_currents, pA_currents, status]}')
                    self.data_sig.emit([pA_currents,pA_currents, status])
                    self.msleep(1000)
                if self._keep_on == 0:
                    self.run_flag = False

def get_COM_port():
    """list all the avialible COM ports  

    Returns:
        dict: {"COM1":Name1, "COM2":Name2, ...}
    """
    Com_list = {}
    port_list = list(serial.tools.list_ports.comports())
    for p in port_list:
        Com_list["%s" % p[0]] = "%s" % p[1]
        print(p[0])
    #print(Com_list)
    return Com_list

if __name__ == '__main__':
    COM_Ports:dict=get_COM_port()
    print(COM_Ports)
    port="COM5"
    Keithley6514 = Keithley6485Com(port=port, func='currents', points=5,full_time=100)
    Keithley6514.open_port(port)
    ID = Keithley6514.deviceID
    version = Keithley6514.version
    print(f'get ID: {ID}\n version:{version}')
    #Keithley6517B.reset()
    Keithley6514.clear_status()
    # Keithley6514.configure_current()
    # Keithley6517B.current_filter()
    # Keithley6517B.curr_medianMode(MediaMode=False)
    # Keithley6517B.current_nplc(nplc=5)
    # Keithley6517B.curr_aver_counts(num=5)

    Keithley6514.zero_check(status='OFF')
    Keithley6514.conf_function('current',wait=100)
    #time.sleep(2)
    i=10
    t_start=time.time()
    while i>0:
        resp = Keithley6514.read_data(wait=100)
        # resp = Keithley6517B.fetch(wait=2000)
        data = Keithley6514.get_value(resp)
        #Keithley6514.start()
        #time.sleep(1)
        i-=1
        print(f'get value:{data:.4e}A')
    print(f'cost:{time.time()-t_start:.4f}s')
    # resp = Keithley6517B.fresh_data()
    # data = Keithley6517B.get_value(resp)
