import math
import time
from pymeasure.instruments.keithley import Keithley6517B
from pymeasure.adapters.serial import SerialAdapter
from pymeasure.adapters.telnet import TelnetAdapter
from PyQt5.QtCore import QTimer, pyqtSlot, QThread, pyqtSignal, QObject
import numpy as np
import pandas as pd
from time import sleep

"""
worker Qthread for reading current[aA~mA] from Keithley 6517B electrometer
"""
PORT = 'ASRL6::INSTR'
HOST = '10.30.95.170'
Port_list = [23, 26, 29, 32]  # port in USR_N540
# pA_PORT=TelnetAdapter(HOST,Port_list[1]) # for connection via USR450_To_RS232/485
pA_PORT = 'ASRL6::INSTR' # for direct connection via RS232/485

class Read6517bCurrent(QThread):
    """
    worker Qthread for reading current[aA~mA] from Keithley 6517B electrometer,using serial port
    emit signal current data when complete:[average,all currents,info]
    """

    data_sig = pyqtSignal(list)

    def __init__(self, port: str = PORT, points: int = 1, delay: float = 0.1, full_time: float = 60, keep_on: int = 0,
                 parent=None):
        #QThread.__init__(self, parent)
        super(Read6517bCurrent, self).__init__(parent)
        # sample points
        self.port = port
        self.points = points
        self.delay = delay
        self.monitor_time = full_time  # monitor for 60s
        self.run_flag = True
        print('ini')
        self.currents = []
        self.sum_current = 0
        self._pAmeter = ''
        # self.pAmeter.reset()
        self._keep_on = keep_on
        print(f'keep on =={keep_on}')
        # set auto range
        # nplc <measurement speed> 0.01 to 10
        # self.pAmeter.measure_current(0.1)

    def __del__(self):
        self.run_flag = False

    def run(self):
        t0 = time.time()
        print(t0)
        self._pAmeter = Keithley6517B(self.port)
        self._pAmeter.measure_current(0.1,10e-12,False)
        while self.run_flag and time.time() - t0 < self.monitor_time:
            try:
                self.sum_current=0
                self.currents=[]
                for i in range(self.points):
                    current = self._pAmeter.current
                    self.currents.append(current)
                    self.sum_current += current
                    time.sleep(self.delay)
            except Exception as e:
                print(e)
            finally:
                if self.currents:
                    average_I = self.sum_current / len(self.currents)
                    info = 'OK'
                    print(f'status:{info} value:{average_I*1000000000000.0:.4f}pA')
                    self.data_sig.emit([average_I,self.currents, info])
                    self.sum_current = 0
                else:
                    info = 'error'
                    self.data_sig.emit([0, 0, info])
                    self.run_flag = False
                if self._keep_on == 0:
                    self.run_flag = False
