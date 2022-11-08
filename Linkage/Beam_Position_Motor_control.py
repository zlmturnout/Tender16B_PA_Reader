from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject
from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
import time, random
import sys, os

"""
This is the control driver file for beam position motor motion control (BPM-X/Z), including PV parameter and QThread 
"""

# PV names for BPM X position
BPM_X_SET = "X20U:SoftEX2:BPM:X.VAL"  # set position
BPM_X_SET_RBV = "X20U:SoftEX2:BPM:X.RBV"  # position read back
BPM_X_SET_MOVN = "X20U:SoftEX2:BPM:X.MOVN"  # motor X moving(0,1)
# PV names for BPM Z position
BPM_Z_SET = "X20U:SoftEX2:BPM:Z.VAL"  # set position
BPM_Z_SET_RBV = "X20U:SoftEX2:BPM:Z.RBV"  # position read back
BPM_Z_SET_MOVN = "X20U:SoftEX2:BPM:Z.MOVN"  # motor Z moving (0,1)


class SetBPMThread(QThread):
    """
    Working QThread for setting position of beam position motor,
    emit done signal when set position is finished successfully.
    emit signal: list[read_back,set_value,check_n,set_info]
    """
    done_signal = Signal(list)

    def __init__(self, set_pv, set_value, rbv_pv, movn_pv, num: int = 0, parent=None):
        """
        need pv name of [set,rbv,mvn] and the set value,num for check usage
        :param set_pv: PV name for set values
        :param set_value: set values
        :param rbv_pv: PV name for read-back values
        :param mov_pv: PV name for motor moving status
        :param num: check num
        :param parent:
        """
        #QThread.__init__(self, parent)
        super().__init__(parent)
        self._set_pv = PV(set_pv)
        self._set_value = set_value
        self._rbv_pv = rbv_pv
        self._check_n = num
        # set the moving
        self._pv_mvn = PV(movn_pv)  # motor moving
        # add callback
        self._pv_mvn.add_callback(self.motor_mvn)
        # flag to determinate the status of put process
        self._motor_mvn_flag = 0
        self._set_flag = False
        # the new read back value and set info
        self._RBK_val = []
        self.set_info = ''

    def run(self):
        t0 = time.time()  # for time out
        print('start setting position:...')
        self._rbv_pv = PV(self._rbv_pv, callback=self.readback_val)
        self._set_flag = True
        if self._set_pv.connect():
            self._set_pv.put(self._set_value)
            print('set value now: %f' % self._set_value)
            self.msleep(500)
            # print('sleep 100ms')
            t_motor=time.time()
            t_motor_timeout=20
            # while self._set_flag and time.time()-t_motor<t_motor_timeout:
            #     # print('sleep 100ms')
            #     self.msleep(200)
            #     # self._MR_mvn_flag=self._MR_mvn.value
            #     print(f'motor status: {self._motor_mvn_flag}')
            #     # check if motor is moving or not
            #     if self._motor_mvn_flag == 1:
            #         self.msleep(300)
            #     elif self._motor_mvn_flag == 0:
            #         print(f'motor stopped: {self._motor_mvn_flag}')
            #         self._set_flag = False
            #         break
            # print('get out and emit signal:')
            # check if the Read_back value have been updated,
            # pv_tem = PV(self._rbv_pv)
            final_pos = self._RBK_val[-1]
            #print(f'final_pos:{final_pos}')
            self.msleep(100)
            t_cur = time.time()
            # Set time out=10s if the target value are not reached
            time_out = 3.0+abs(final_pos-self._set_value)*0.005
            while time.time() - t_cur < time_out:
                # print('sleep')
                if abs(final_pos - self._set_value) < 1:
                    t_jump = time.time()
                    self.set_info = 'done'
                    break
                else:
                    self.msleep(100)
                    #pv_tem = PV(self._rbv_pv)
                    final_pos = self._RBK_val[-1]
                    t_jump = time.time()
                    self.set_info = f'done with time out:{time_out}'
            # jump out time
            print(f'jump out after: {t_jump - t_cur:.2f}s with time out of {time_out}s')
            info = [final_pos, self._set_value, self._check_n, self.set_info]
            print(info)
            print(f'set position done in {(t_jump - t0):.2f} seconds ')
            self._rbv_pv.remove_callback()
            self.msleep(200)
            self.done_signal.emit(info)

    def readback_val(self, pvname, value, **kwargs):
        """
        read back value
        :return:
        """
        if value:
            self._RBK_val.append(value)
            # print(self._RBK_val)
            # print(f'call back get: {value}')

    def motor_mvn(self, pvname, value, **kw):
        """
        callback when mirror moving, 0 is stop,1 is moving
        :return:
        """
        if value:
            print(f'Motor status: {value}')
            self._motor_mvn_flag = value
