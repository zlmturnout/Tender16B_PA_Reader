import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# pyinstaller -w -D .\BPM_plot_new.py --clean --hidden-import epics --hidden-import epics.clibs