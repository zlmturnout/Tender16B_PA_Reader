import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets

"""
notes
My matplotlib pyqt5 widgets
"""


# text='LIMIN_ZHOU_at_SSRF_BL20U'
# f'{text:#^100s}'

# ###########################LIMIN_Zhou_at_SSRF_BL20U############################
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&LIMIN_Zhou_at_SSRF_BL20U&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************


# class Myplot for plotting with matplotlib
class Myplot(FigureCanvas):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        # normalized for 中文显示和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # new figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # activate figure window
        # super(Plot_dynamic,self).__init__(self.fig)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # sub plot by self.axes
        self.axes = self.fig.add_subplot(111)
        # initial figure
        self.compute_initial_figure()
        # size policy
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


# specialized for A_in plot
class InitialPlot(Myplot):
    def __init__(self, *args, **kwargs):
        Myplot.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        counts = [0, 1]
        delay_t = [0, 1]
        # add NavigationToolbar in the figure (widgets)
        self.axes.plot(delay_t, counts, '-ob')
        self.axes.set_yticks([-1, 0, 1])
        self.axes.set_title("Counter Read", fontsize=20)
        self.axes.set_xlabel("delay(s)", fontsize=20)
        self.axes.set_ylabel("Counts", fontsize=20)


# class Myplot for plotting with matplotlib
class MonitorPlot(FigureCanvas):
    def __init__(self, parent=None, width=3, height=3, dpi=72):
        # normalized for 中文显示和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # new figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # activate figure window
        # super(Plot_dynamic,self).__init__(self.fig)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # sub plot by self.axes
        self.axes = self.fig.add_subplot(111)
        # initial figure
        self.compute_initial_figure()
        # size policy
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass
