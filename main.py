import PySide6,sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
    
from T16B_BeamCurrent_plot import *

"""Main entrance  

Start Project program
"""

"""
for bat file:

@echo off
E:
cd E:\Coding\Eline20U_Control\Beam_Position_Motion
start python main.py
pause

"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PMCMotionPlot()
    win.show()
    sys.exit(app.exec())