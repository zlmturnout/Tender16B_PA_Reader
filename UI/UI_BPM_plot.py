# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_BPM_plot.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
import qpprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1453, 838)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.actionView_data = QAction(MainWindow)
        self.actionView_data.setObjectName(u"actionView_data")
        self.actionPMC_motor = QAction(MainWindow)
        self.actionPMC_motor.setObjectName(u"actionPMC_motor")
        self.actionpAmeter = QAction(MainWindow)
        self.actionpAmeter.setObjectName(u"actionpAmeter")
        self.actionDatabase = QAction(MainWindow)
        self.actionDatabase.setObjectName(u"actionDatabase")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 106, 60, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(85, 170, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_2.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.Channel_cbx = QComboBox(self.centralwidget)
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.setObjectName(u"Channel_cbx")
        self.Channel_cbx.setMinimumSize(QSize(100, 40))
        self.Channel_cbx.setMaximumSize(QSize(220, 16777215))
        palette1 = QPalette()
        brush5 = QBrush(QColor(255, 85, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(180, 249, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush7 = QBrush(QColor(255, 0, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        brush8 = QBrush(QColor(240, 240, 240, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        brush9 = QBrush(QColor(0, 120, 215, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Channel_cbx.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Channel_cbx.setFont(font1)
        self.Channel_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Channel_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_3.addWidget(self.Channel_cbx)

        self.Connect_pmc_btn = QPushButton(self.centralwidget)
        self.Connect_pmc_btn.setObjectName(u"Connect_pmc_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Connect_pmc_btn.sizePolicy().hasHeightForWidth())
        self.Connect_pmc_btn.setSizePolicy(sizePolicy1)
        self.Connect_pmc_btn.setMinimumSize(QSize(100, 40))
        self.Connect_pmc_btn.setMaximumSize(QSize(220, 16777215))
        self.Connect_pmc_btn.setFont(font)
        self.Connect_pmc_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_3.addWidget(self.Connect_pmc_btn)

        self.Port_cbx = QComboBox(self.centralwidget)
        self.Port_cbx.setObjectName(u"Port_cbx")
        self.Port_cbx.setMinimumSize(QSize(150, 40))
        self.Port_cbx.setMaximumSize(QSize(220, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.Port_cbx.setFont(font2)
        self.Port_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Port_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_3.addWidget(self.Port_cbx)

        self.Connect_pAmeter_btn = QPushButton(self.centralwidget)
        self.Connect_pAmeter_btn.setObjectName(u"Connect_pAmeter_btn")
        sizePolicy1.setHeightForWidth(self.Connect_pAmeter_btn.sizePolicy().hasHeightForWidth())
        self.Connect_pAmeter_btn.setSizePolicy(sizePolicy1)
        self.Connect_pAmeter_btn.setMinimumSize(QSize(140, 40))
        self.Connect_pAmeter_btn.setMaximumSize(QSize(220, 16777215))
        self.Connect_pAmeter_btn.setFont(font)
        self.Connect_pAmeter_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_3.addWidget(self.Connect_pAmeter_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.Input_scan_range_btn = QPushButton(self.centralwidget)
        self.Input_scan_range_btn.setObjectName(u"Input_scan_range_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Input_scan_range_btn.sizePolicy().hasHeightForWidth())
        self.Input_scan_range_btn.setSizePolicy(sizePolicy2)
        self.Input_scan_range_btn.setMinimumSize(QSize(180, 40))
        self.Input_scan_range_btn.setMaximumSize(QSize(250, 16777215))
        palette2 = QPalette()
        brush10 = QBrush(QColor(255, 255, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        brush11 = QBrush(QColor(0, 170, 127, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush11)
        brush12 = QBrush(QColor(208, 113, 87, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Input_scan_range_btn.setPalette(palette2)
        self.Input_scan_range_btn.setFont(font)
        self.Input_scan_range_btn.setStyleSheet(u"\n"
"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 3"
                        "3);}")

        self.horizontalLayout_3.addWidget(self.Input_scan_range_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.Plot_box = QGroupBox(self.centralwidget)
        self.Plot_box.setObjectName(u"Plot_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Plot_box.sizePolicy().hasHeightForWidth())
        self.Plot_box.setSizePolicy(sizePolicy3)
        self.Plot_box.setMinimumSize(QSize(800, 500))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.Plot_box.setFont(font3)
        self.Plot_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout.addWidget(self.Plot_box)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.groupBox.setMinimumSize(QSize(800, 60))
        self.groupBox.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0882353 rgba(64, 252, 255, 200), stop:0.333333 rgba(119, 241, 255, 200), stop:0.588235 rgba(170, 255, 255, 200), stop:0.897059 rgba(190, 255, 244, 200));\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.Start_plot = QPushButton(self.groupBox)
        self.Start_plot.setObjectName(u"Start_plot")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Start_plot.sizePolicy().hasHeightForWidth())
        self.Start_plot.setSizePolicy(sizePolicy5)
        self.Start_plot.setMinimumSize(QSize(100, 50))
        palette3 = QPalette()
        brush13 = QBrush(QColor(255, 113, 84, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        brush14 = QBrush(QColor(35, 202, 166, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush10)
        brush15 = QBrush(QColor(127, 127, 127, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(170, 170, 170, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush14)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush17)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush12)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush17)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.Start_plot.setPalette(palette3)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.Start_plot.setFont(font4)
        self.Start_plot.setFocusPolicy(Qt.ClickFocus)
        self.Start_plot.setStyleSheet(u"\n"
"QPushButton{background-color:  rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 113, 84);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, "
                        "33);}")
        self.Start_plot.setCheckable(False)
        self.Start_plot.setAutoDefault(False)
        self.Start_plot.setFlat(False)

        self.horizontalLayout_5.addWidget(self.Start_plot)

        self.horizontalSpacer_8 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.Stop_plot = QPushButton(self.groupBox)
        self.Stop_plot.setObjectName(u"Stop_plot")
        sizePolicy5.setHeightForWidth(self.Stop_plot.sizePolicy().hasHeightForWidth())
        self.Stop_plot.setSizePolicy(sizePolicy5)
        self.Stop_plot.setMinimumSize(QSize(100, 50))
        self.Stop_plot.setFont(font4)
        self.Stop_plot.setFocusPolicy(Qt.WheelFocus)
        self.Stop_plot.setStyleSheet(u"QPushButton{background-color:  rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 117, 0) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_5.addWidget(self.Stop_plot)

        self.horizontalSpacer_9 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.Clear_Save = QPushButton(self.groupBox)
        self.Clear_Save.setObjectName(u"Clear_Save")
        sizePolicy5.setHeightForWidth(self.Clear_Save.sizePolicy().hasHeightForWidth())
        self.Clear_Save.setSizePolicy(sizePolicy5)
        self.Clear_Save.setMinimumSize(QSize(100, 50))
        self.Clear_Save.setFont(font4)
        self.Clear_Save.setStyleSheet(u"\n"
"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 113, 84);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 3"
                        "3);}\n"
"")

        self.horizontalLayout_5.addWidget(self.Clear_Save)

        self.horizontalSpacer_10 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.Caculate = QPushButton(self.groupBox)
        self.Caculate.setObjectName(u"Caculate")
        sizePolicy5.setHeightForWidth(self.Caculate.sizePolicy().hasHeightForWidth())
        self.Caculate.setSizePolicy(sizePolicy5)
        self.Caculate.setMinimumSize(QSize(100, 50))
        self.Caculate.setFont(font4)
        self.Caculate.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 113, 84);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_5.addWidget(self.Caculate)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addWidget(self.groupBox)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Now_T = QLabel(self.centralwidget)
        self.Now_T.setObjectName(u"Now_T")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Now_T.sizePolicy().hasHeightForWidth())
        self.Now_T.setSizePolicy(sizePolicy6)
        self.Now_T.setMinimumSize(QSize(250, 30))
        self.Now_T.setMaximumSize(QSize(1000, 40))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        brush18 = QBrush(QColor(44, 213, 196, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush18)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush18)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Now_T.setPalette(palette4)
        self.Now_T.setFont(font)
        self.Now_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Now_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Now_T)

        self.Expect_FN_T = QLabel(self.centralwidget)
        self.Expect_FN_T.setObjectName(u"Expect_FN_T")
        sizePolicy6.setHeightForWidth(self.Expect_FN_T.sizePolicy().hasHeightForWidth())
        self.Expect_FN_T.setSizePolicy(sizePolicy6)
        self.Expect_FN_T.setMinimumSize(QSize(250, 30))
        self.Expect_FN_T.setMaximumSize(QSize(1000, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Expect_FN_T.setPalette(palette5)
        self.Expect_FN_T.setFont(font)
        self.Expect_FN_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Expect_FN_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Expect_FN_T)

        self.Done_time = QLabel(self.centralwidget)
        self.Done_time.setObjectName(u"Done_time")
        sizePolicy6.setHeightForWidth(self.Done_time.sizePolicy().hasHeightForWidth())
        self.Done_time.setSizePolicy(sizePolicy6)
        self.Done_time.setMinimumSize(QSize(250, 30))
        self.Done_time.setMaximumSize(QSize(1000, 40))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Done_time.setPalette(palette6)
        self.Done_time.setFont(font)
        self.Done_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Done_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Done_time)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Select_instruments = QTabWidget(self.centralwidget)
        self.Select_instruments.setObjectName(u"Select_instruments")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Select_instruments.sizePolicy().hasHeightForWidth())
        self.Select_instruments.setSizePolicy(sizePolicy7)
        self.Select_instruments.setMinimumSize(QSize(0, 326))
        self.Select_instruments.setMaximumSize(QSize(450, 800))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        brush19 = QBrush(QColor(255, 85, 0, 128))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Select_instruments.setPalette(palette7)
        self.Select_instruments.setFont(font)
        self.Select_instruments.setTabPosition(QTabWidget.North)
        self.Select_instruments.setTabShape(QTabWidget.Rounded)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pAmeter_plot = QGroupBox(self.tab_4)
        self.pAmeter_plot.setObjectName(u"pAmeter_plot")
        sizePolicy7.setHeightForWidth(self.pAmeter_plot.sizePolicy().hasHeightForWidth())
        self.pAmeter_plot.setSizePolicy(sizePolicy7)
        self.pAmeter_plot.setMinimumSize(QSize(400, 150))
        self.pAmeter_plot.setMaximumSize(QSize(400, 16777215))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.pAmeter_plot.setPalette(palette8)
        self.pAmeter_plot.setFont(font1)

        self.verticalLayout_2.addWidget(self.pAmeter_plot)

        self.Adc_box_2 = QGroupBox(self.tab_4)
        self.Adc_box_2.setObjectName(u"Adc_box_2")
        sizePolicy5.setHeightForWidth(self.Adc_box_2.sizePolicy().hasHeightForWidth())
        self.Adc_box_2.setSizePolicy(sizePolicy5)
        self.Adc_box_2.setMinimumSize(QSize(400, 100))
        self.Adc_box_2.setMaximumSize(QSize(400, 16777215))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_2.setPalette(palette9)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.Adc_box_2.setFont(font5)
        self.gridLayout = QGridLayout(self.Adc_box_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.lcd_pA = QLCDNumber(self.Adc_box_2)
        self.lcd_pA.setObjectName(u"lcd_pA")
        sizePolicy5.setHeightForWidth(self.lcd_pA.sizePolicy().hasHeightForWidth())
        self.lcd_pA.setSizePolicy(sizePolicy5)
        self.lcd_pA.setMinimumSize(QSize(120, 30))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_pA.setPalette(palette10)
        self.lcd_pA.setDigitCount(8)
        self.lcd_pA.setSegmentStyle(QLCDNumber.Filled)

        self.horizontalLayout_7.addWidget(self.lcd_pA)

        self.Current_label = QLabel(self.Adc_box_2)
        self.Current_label.setObjectName(u"Current_label")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Current_label.setPalette(palette11)
        self.Current_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.Current_label)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_19)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_20 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_20)

        self.Monitor_pA = QPushButton(self.Adc_box_2)
        self.Monitor_pA.setObjectName(u"Monitor_pA")
        sizePolicy7.setHeightForWidth(self.Monitor_pA.sizePolicy().hasHeightForWidth())
        self.Monitor_pA.setSizePolicy(sizePolicy7)
        self.Monitor_pA.setMinimumSize(QSize(75, 40))
        self.Monitor_pA.setFont(font1)
        self.Monitor_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.Monitor_pA.setFlat(False)

        self.horizontalLayout_8.addWidget(self.Monitor_pA)

        self.horizontalSpacer_21 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_21)

        self.Stop_Monitor_pA = QPushButton(self.Adc_box_2)
        self.Stop_Monitor_pA.setObjectName(u"Stop_Monitor_pA")
        sizePolicy7.setHeightForWidth(self.Stop_Monitor_pA.sizePolicy().hasHeightForWidth())
        self.Stop_Monitor_pA.setSizePolicy(sizePolicy7)
        self.Stop_Monitor_pA.setMinimumSize(QSize(75, 40))
        self.Stop_Monitor_pA.setFont(font1)
        self.Stop_Monitor_pA.setStyleSheet(u"QPushButton{background-color:  rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 85, 127) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);"
                        "}")

        self.horizontalLayout_8.addWidget(self.Stop_Monitor_pA)

        self.horizontalSpacer_22 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_22)

        self.Clear_Monitor_pA = QPushButton(self.Adc_box_2)
        self.Clear_Monitor_pA.setObjectName(u"Clear_Monitor_pA")
        sizePolicy7.setHeightForWidth(self.Clear_Monitor_pA.sizePolicy().hasHeightForWidth())
        self.Clear_Monitor_pA.setSizePolicy(sizePolicy7)
        self.Clear_Monitor_pA.setMinimumSize(QSize(75, 40))
        self.Clear_Monitor_pA.setFont(font1)
        self.Clear_Monitor_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_8.addWidget(self.Clear_Monitor_pA)

        self.horizontalSpacer_23 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_23)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.Adc_box_2)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.Select_instruments.addTab(self.tab_4, "")

        self.verticalLayout_6.addWidget(self.Select_instruments)

        self.Channel_tabs = QTabWidget(self.centralwidget)
        self.Channel_tabs.setObjectName(u"Channel_tabs")
        sizePolicy7.setHeightForWidth(self.Channel_tabs.sizePolicy().hasHeightForWidth())
        self.Channel_tabs.setSizePolicy(sizePolicy7)
        self.Channel_tabs.setMinimumSize(QSize(430, 300))
        self.Channel_tabs.setMaximumSize(QSize(450, 800))
        self.Channel_tabs.setSizeIncrement(QSize(100, 100))
        self.Channel_tabs.setBaseSize(QSize(50, 50))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Channel_tabs.setPalette(palette12)
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.Channel_tabs.setFont(font6)
        self.Channel_tabs.setStyleSheet(u"")
        self.Channel_tabs.setTabPosition(QTabWidget.South)
        self.Channel_tabs.setTabShape(QTabWidget.Rounded)
        self.Channel_tabs.setUsesScrollButtons(False)
        self.Channel_tabs.setDocumentMode(False)
        self.Channel_tabs.setTabsClosable(False)
        self.Channel_tabs.setMovable(False)
        self.Channel_tabs.setTabBarAutoHide(False)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ch_position = QGroupBox(self.tab_3)
        self.ch_position.setObjectName(u"ch_position")
        sizePolicy7.setHeightForWidth(self.ch_position.sizePolicy().hasHeightForWidth())
        self.ch_position.setSizePolicy(sizePolicy7)
        self.ch_position.setMinimumSize(QSize(400, 150))
        palette13 = QPalette()
        brush20 = QBrush(QColor(255, 170, 0, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.ch_position.setPalette(palette13)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        self.ch_position.setFont(font7)

        self.gridLayout_5.addWidget(self.ch_position, 0, 0, 1, 1)

        self.Adc_box_5 = QGroupBox(self.tab_3)
        self.Adc_box_5.setObjectName(u"Adc_box_5")
        sizePolicy5.setHeightForWidth(self.Adc_box_5.sizePolicy().hasHeightForWidth())
        self.Adc_box_5.setSizePolicy(sizePolicy5)
        self.Adc_box_5.setMinimumSize(QSize(400, 125))
        self.Adc_box_5.setMaximumSize(QSize(400, 16777215))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_5.setPalette(palette14)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setStyleStrategy(QFont.PreferAntialias)
        self.Adc_box_5.setFont(font8)
        self.verticalLayout_7 = QVBoxLayout(self.Adc_box_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.lcd_ch_pos = QLCDNumber(self.Adc_box_5)
        self.lcd_ch_pos.setObjectName(u"lcd_ch_pos")
        sizePolicy5.setHeightForWidth(self.lcd_ch_pos.sizePolicy().hasHeightForWidth())
        self.lcd_ch_pos.setSizePolicy(sizePolicy5)
        self.lcd_ch_pos.setMinimumSize(QSize(120, 30))
        palette15 = QPalette()
        brush21 = QBrush(QColor(255, 85, 255, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.lcd_ch_pos.setPalette(palette15)
        self.lcd_ch_pos.setDigitCount(8)

        self.horizontalLayout_10.addWidget(self.lcd_ch_pos)

        self.label_6 = QLabel(self.Adc_box_5)
        self.label_6.setObjectName(u"label_6")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_6.setPalette(palette16)
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setStyleStrategy(QFont.PreferAntialias)
        self.label_6.setFont(font9)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.Plot_x_cbx = QComboBox(self.Adc_box_5)
        self.Plot_x_cbx.addItem("")
        self.Plot_x_cbx.addItem("")
        self.Plot_x_cbx.setObjectName(u"Plot_x_cbx")
        self.Plot_x_cbx.setMinimumSize(QSize(80, 30))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        self.Plot_x_cbx.setPalette(palette17)

        self.horizontalLayout_10.addWidget(self.Plot_x_cbx)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ch_pos_left = QPushButton(self.Adc_box_5)
        self.ch_pos_left.setObjectName(u"ch_pos_left")
        sizePolicy7.setHeightForWidth(self.ch_pos_left.sizePolicy().hasHeightForWidth())
        self.ch_pos_left.setSizePolicy(sizePolicy7)
        self.ch_pos_left.setMinimumSize(QSize(60, 40))
        self.ch_pos_left.setMaximumSize(QSize(16777215, 40))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush14)
        brush22 = QBrush(QColor(255, 85, 127, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Active, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.ch_pos_left.setPalette(palette18)
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(28)
        font10.setBold(False)
        font10.setStyleStrategy(QFont.PreferDefault)
        self.ch_pos_left.setFont(font10)
        self.ch_pos_left.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.ch_pos_left.setAutoDefault(False)
        self.ch_pos_left.setFlat(False)

        self.horizontalLayout_11.addWidget(self.ch_pos_left)

        self.Step_ch_pos = QDoubleSpinBox(self.Adc_box_5)
        self.Step_ch_pos.setObjectName(u"Step_ch_pos")
        sizePolicy5.setHeightForWidth(self.Step_ch_pos.sizePolicy().hasHeightForWidth())
        self.Step_ch_pos.setSizePolicy(sizePolicy5)
        self.Step_ch_pos.setMinimumSize(QSize(160, 40))
        self.Step_ch_pos.setMaximumSize(QSize(16777215, 40))
        self.Step_ch_pos.setFont(font6)
        self.Step_ch_pos.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhNoAutoUppercase|Qt.ImhPreferNumbers)
        self.Step_ch_pos.setAlignment(Qt.AlignCenter)
        self.Step_ch_pos.setDecimals(1)
        self.Step_ch_pos.setMinimum(0.100000000000000)
        self.Step_ch_pos.setMaximum(10000.000000000000000)
        self.Step_ch_pos.setSingleStep(1.000000000000000)
        self.Step_ch_pos.setValue(1.100000000000000)

        self.horizontalLayout_11.addWidget(self.Step_ch_pos)

        self.ch_pos_right = QPushButton(self.Adc_box_5)
        self.ch_pos_right.setObjectName(u"ch_pos_right")
        sizePolicy7.setHeightForWidth(self.ch_pos_right.sizePolicy().hasHeightForWidth())
        self.ch_pos_right.setSizePolicy(sizePolicy7)
        self.ch_pos_right.setMinimumSize(QSize(60, 40))
        self.ch_pos_right.setMaximumSize(QSize(16777215, 40))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Active, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.ch_pos_right.setPalette(palette19)
        self.ch_pos_right.setFont(font10)
        self.ch_pos_right.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_11.addWidget(self.ch_pos_right)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.gridLayout_5.addWidget(self.Adc_box_5, 1, 0, 1, 1)

        self.Channel_tabs.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.X_position = QGroupBox(self.tab_2)
        self.X_position.setObjectName(u"X_position")
        sizePolicy7.setHeightForWidth(self.X_position.sizePolicy().hasHeightForWidth())
        self.X_position.setSizePolicy(sizePolicy7)
        self.X_position.setMinimumSize(QSize(400, 150))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.X_position.setPalette(palette20)
        self.X_position.setFont(font7)

        self.verticalLayout_5.addWidget(self.X_position)

        self.Adc_box_3 = QGroupBox(self.tab_2)
        self.Adc_box_3.setObjectName(u"Adc_box_3")
        sizePolicy5.setHeightForWidth(self.Adc_box_3.sizePolicy().hasHeightForWidth())
        self.Adc_box_3.setSizePolicy(sizePolicy5)
        self.Adc_box_3.setMinimumSize(QSize(400, 125))
        self.Adc_box_3.setMaximumSize(QSize(400, 16777215))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_3.setPalette(palette21)
        self.Adc_box_3.setFont(font8)
        self.verticalLayout_4 = QVBoxLayout(self.Adc_box_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.lcd_X_pos = QLCDNumber(self.Adc_box_3)
        self.lcd_X_pos.setObjectName(u"lcd_X_pos")
        sizePolicy5.setHeightForWidth(self.lcd_X_pos.sizePolicy().hasHeightForWidth())
        self.lcd_X_pos.setSizePolicy(sizePolicy5)
        self.lcd_X_pos.setMinimumSize(QSize(120, 30))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_X_pos.setPalette(palette22)
        self.lcd_X_pos.setDigitCount(8)
        self.lcd_X_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_9.addWidget(self.lcd_X_pos)

        self.label_5 = QLabel(self.Adc_box_3)
        self.label_5.setObjectName(u"label_5")
        palette23 = QPalette()
        brush23 = QBrush(QColor(0, 170, 255, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush23)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush23)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_5.setPalette(palette23)
        self.label_5.setFont(font9)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.X_pos_left = QPushButton(self.Adc_box_3)
        self.X_pos_left.setObjectName(u"X_pos_left")
        sizePolicy7.setHeightForWidth(self.X_pos_left.sizePolicy().hasHeightForWidth())
        self.X_pos_left.setSizePolicy(sizePolicy7)
        self.X_pos_left.setMinimumSize(QSize(60, 40))
        self.X_pos_left.setMaximumSize(QSize(16777215, 40))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette24.setBrush(QPalette.Active, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.X_pos_left.setPalette(palette24)
        self.X_pos_left.setFont(font10)
        self.X_pos_left.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.X_pos_left.setAutoDefault(False)
        self.X_pos_left.setFlat(False)

        self.horizontalLayout.addWidget(self.X_pos_left)

        self.Step_X_pos = QDoubleSpinBox(self.Adc_box_3)
        self.Step_X_pos.setObjectName(u"Step_X_pos")
        sizePolicy5.setHeightForWidth(self.Step_X_pos.sizePolicy().hasHeightForWidth())
        self.Step_X_pos.setSizePolicy(sizePolicy5)
        self.Step_X_pos.setMinimumSize(QSize(200, 40))
        self.Step_X_pos.setFont(font6)
        self.Step_X_pos.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhNoAutoUppercase|Qt.ImhPreferNumbers)
        self.Step_X_pos.setAlignment(Qt.AlignCenter)
        self.Step_X_pos.setDecimals(0)
        self.Step_X_pos.setMinimum(0.000000000000000)
        self.Step_X_pos.setMaximum(10000.000000000000000)
        self.Step_X_pos.setSingleStep(1.000000000000000)
        self.Step_X_pos.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.Step_X_pos)

        self.X_pos_right = QPushButton(self.Adc_box_3)
        self.X_pos_right.setObjectName(u"X_pos_right")
        sizePolicy7.setHeightForWidth(self.X_pos_right.sizePolicy().hasHeightForWidth())
        self.X_pos_right.setSizePolicy(sizePolicy7)
        self.X_pos_right.setMinimumSize(QSize(60, 40))
        self.X_pos_right.setMaximumSize(QSize(60, 40))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette25.setBrush(QPalette.Active, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.X_pos_right.setPalette(palette25)
        self.X_pos_right.setFont(font10)
        self.X_pos_right.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout.addWidget(self.X_pos_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.Adc_box_3)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.Channel_tabs.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Z_position = QGroupBox(self.tab)
        self.Z_position.setObjectName(u"Z_position")
        sizePolicy7.setHeightForWidth(self.Z_position.sizePolicy().hasHeightForWidth())
        self.Z_position.setSizePolicy(sizePolicy7)
        self.Z_position.setMinimumSize(QSize(400, 150))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Z_position.setPalette(palette26)
        self.Z_position.setFont(font7)

        self.gridLayout_2.addWidget(self.Z_position, 0, 0, 1, 1)

        self.Adc_box_4 = QGroupBox(self.tab)
        self.Adc_box_4.setObjectName(u"Adc_box_4")
        sizePolicy5.setHeightForWidth(self.Adc_box_4.sizePolicy().hasHeightForWidth())
        self.Adc_box_4.setSizePolicy(sizePolicy5)
        self.Adc_box_4.setMinimumSize(QSize(400, 125))
        self.Adc_box_4.setMaximumSize(QSize(400, 16777215))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_4.setPalette(palette27)
        self.Adc_box_4.setFont(font8)
        self.verticalLayout_3 = QVBoxLayout(self.Adc_box_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.lcd_Z_pos = QLCDNumber(self.Adc_box_4)
        self.lcd_Z_pos.setObjectName(u"lcd_Z_pos")
        sizePolicy5.setHeightForWidth(self.lcd_Z_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Z_pos.setSizePolicy(sizePolicy5)
        self.lcd_Z_pos.setMinimumSize(QSize(120, 30))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.lcd_Z_pos.setPalette(palette28)
        self.lcd_Z_pos.setDigitCount(8)

        self.horizontalLayout_6.addWidget(self.lcd_Z_pos)

        self.label_4 = QLabel(self.Adc_box_4)
        self.label_4.setObjectName(u"label_4")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_4.setPalette(palette29)
        self.label_4.setFont(font9)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Z_pos_left = QPushButton(self.Adc_box_4)
        self.Z_pos_left.setObjectName(u"Z_pos_left")
        sizePolicy7.setHeightForWidth(self.Z_pos_left.sizePolicy().hasHeightForWidth())
        self.Z_pos_left.setSizePolicy(sizePolicy7)
        self.Z_pos_left.setMinimumSize(QSize(60, 40))
        self.Z_pos_left.setMaximumSize(QSize(16777215, 40))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette30.setBrush(QPalette.Active, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette30.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette30.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Z_pos_left.setPalette(palette30)
        self.Z_pos_left.setFont(font10)
        self.Z_pos_left.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.Z_pos_left.setAutoDefault(False)
        self.Z_pos_left.setFlat(False)

        self.horizontalLayout_2.addWidget(self.Z_pos_left)

        self.Step_Z_pos = QDoubleSpinBox(self.Adc_box_4)
        self.Step_Z_pos.setObjectName(u"Step_Z_pos")
        sizePolicy5.setHeightForWidth(self.Step_Z_pos.sizePolicy().hasHeightForWidth())
        self.Step_Z_pos.setSizePolicy(sizePolicy5)
        self.Step_Z_pos.setMinimumSize(QSize(160, 40))
        self.Step_Z_pos.setMaximumSize(QSize(16777215, 40))
        self.Step_Z_pos.setFont(font6)
        self.Step_Z_pos.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhNoAutoUppercase|Qt.ImhPreferNumbers)
        self.Step_Z_pos.setAlignment(Qt.AlignCenter)
        self.Step_Z_pos.setDecimals(0)
        self.Step_Z_pos.setMinimum(1.000000000000000)
        self.Step_Z_pos.setMaximum(500000.000000000000000)
        self.Step_Z_pos.setSingleStep(1.000000000000000)
        self.Step_Z_pos.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.Step_Z_pos)

        self.Z_pos_right = QPushButton(self.Adc_box_4)
        self.Z_pos_right.setObjectName(u"Z_pos_right")
        sizePolicy7.setHeightForWidth(self.Z_pos_right.sizePolicy().hasHeightForWidth())
        self.Z_pos_right.setSizePolicy(sizePolicy7)
        self.Z_pos_right.setMinimumSize(QSize(60, 40))
        self.Z_pos_right.setMaximumSize(QSize(16777215, 40))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette31.setBrush(QPalette.Active, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette31.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette31.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Z_pos_right.setPalette(palette31)
        self.Z_pos_right.setFont(font10)
        self.Z_pos_right.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_2.addWidget(self.Z_pos_right)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.Adc_box_4, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.Channel_tabs.addTab(self.tab, "")

        self.verticalLayout_6.addWidget(self.Channel_tabs)

        self.Msg_box = QTextBrowser(self.centralwidget)
        self.Msg_box.setObjectName(u"Msg_box")
        self.Msg_box.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.Msg_box.sizePolicy().hasHeightForWidth())
        self.Msg_box.setSizePolicy(sizePolicy8)
        self.Msg_box.setMinimumSize(QSize(430, 100))
        self.Msg_box.setMaximumSize(QSize(450, 200))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Text, brush11)
        brush24 = QBrush(QColor(0, 0, 0, 255))
        brush24.setStyle(Qt.NoBrush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush24)
        brush25 = QBrush(QColor(0, 170, 255, 128))
        brush25.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush25)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        brush26 = QBrush(QColor(0, 0, 0, 255))
        brush26.setStyle(Qt.NoBrush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush25)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush27 = QBrush(QColor(0, 0, 0, 255))
        brush27.setStyle(Qt.NoBrush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush27)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Msg_box.setPalette(palette32)
        self.Msg_box.setFont(font)
        self.Msg_box.setStyleSheet(u"background-image:url(:/icons/icons/my_style_signature.png)\n"
"")

        self.verticalLayout_6.addWidget(self.Msg_box)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1453, 28))
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy9)
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setSizeIncrement(QSize(0, 0))
        self.menubar.setBaseSize(QSize(0, 0))
        palette33 = QPalette()
        self.menubar.setPalette(palette33)
        self.menubar.setFont(font)
        self.menubar.setDefaultUp(False)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(342, 306, 163, 50))
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.menuMenu.sizePolicy().hasHeightForWidth())
        self.menuMenu.setSizePolicy(sizePolicy10)
        self.menuMenu.setMinimumSize(QSize(120, 50))
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(12)
        font11.setBold(False)
        self.menuMenu.setFont(font11)
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.Text, brush11)
        brush28 = QBrush(QColor(0, 170, 127, 128))
        brush28.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        brush29 = QBrush(QColor(109, 109, 109, 255))
        brush29.setStyle(Qt.SolidPattern)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush29)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menuAnalysis.setPalette(palette34)
        self.menuAnalysis.setFont(font11)
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.Text, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush29)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menuInstrument.setPalette(palette35)
        self.menuInstrument.setFont(font11)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuInstrument.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuAnalysis.addAction(self.actionView_data)
        self.menuAnalysis.addAction(self.actionDatabase)
        self.menuInstrument.addAction(self.actionPMC_motor)
        self.menuInstrument.addAction(self.actionpAmeter)

        self.retranslateUi(MainWindow)

        self.Start_plot.setDefault(False)
        self.Select_instruments.setCurrentIndex(0)
        self.Channel_tabs.setCurrentIndex(0)
        self.ch_pos_left.setDefault(False)
        self.X_pos_left.setDefault(False)
        self.Z_pos_left.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionView_data.setText(QCoreApplication.translate("MainWindow", u"View data", None))
        self.actionPMC_motor.setText(QCoreApplication.translate("MainWindow", u"PMC_motor", None))
        self.actionpAmeter.setText(QCoreApplication.translate("MainWindow", u"pAmeter", None))
        self.actionDatabase.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.Channel_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"Energy", None))
        self.Channel_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"BPM_X", None))
        self.Channel_cbx.setItemText(2, QCoreApplication.translate("MainWindow", u"BPM_Z", None))

#if QT_CONFIG(tooltip)
        self.Connect_pmc_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Electrometer6514", None))
#endif // QT_CONFIG(tooltip)
        self.Connect_pmc_btn.setText(QCoreApplication.translate("MainWindow", u"Connect motor", None))
#if QT_CONFIG(tooltip)
        self.Connect_pAmeter_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Electrometer6514", None))
#endif // QT_CONFIG(tooltip)
        self.Connect_pAmeter_btn.setText(QCoreApplication.translate("MainWindow", u"Connect 6514", None))
        self.Input_scan_range_btn.setText(QCoreApplication.translate("MainWindow", u"Input Scan Range", None))
#if QT_CONFIG(statustip)
        self.Plot_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot_area", None))
#endif // QT_CONFIG(statustip)
        self.Plot_box.setTitle(QCoreApplication.translate("MainWindow", u"BeamSize_plot", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.Start_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Start_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"begin scan,should choose scan mode and scan range", None))
#endif // QT_CONFIG(statustip)
        self.Start_plot.setText(QCoreApplication.translate("MainWindow", u"Start_plot", None))
#if QT_CONFIG(tooltip)
        self.Stop_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Stop_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"Stop scan", None))
#endif // QT_CONFIG(statustip)
        self.Stop_plot.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.Clear_Save.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Clear_Save.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear data in the plot and save ", None))
#endif // QT_CONFIG(statustip)
        self.Clear_Save.setText(QCoreApplication.translate("MainWindow", u"Clear+Save", None))
#if QT_CONFIG(tooltip)
        self.Caculate.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Caculate.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate fit", None))
#endif // QT_CONFIG(statustip)
        self.Caculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.Now_T.setText(QCoreApplication.translate("MainWindow", u"Now", None))
        self.Expect_FN_T.setText("")
        self.Done_time.setText("")
        self.pAmeter_plot.setTitle(QCoreApplication.translate("MainWindow", u"pA_plot", None))
        self.Adc_box_2.setTitle(QCoreApplication.translate("MainWindow", u"pA 6514", None))
#if QT_CONFIG(tooltip)
        self.lcd_pA.setToolTip(QCoreApplication.translate("MainWindow", u"read value", None))
#endif // QT_CONFIG(tooltip)
        self.Current_label.setText(QCoreApplication.translate("MainWindow", u"pA", None))
        self.Monitor_pA.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.Stop_Monitor_pA.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Clear_Monitor_pA.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Select_instruments.setTabText(self.Select_instruments.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"pAmeter", None))
        self.ch_position.setTitle(QCoreApplication.translate("MainWindow", u"channel", None))
        self.Adc_box_5.setTitle(QCoreApplication.translate("MainWindow", u"ch_set", None))
#if QT_CONFIG(tooltip)
        self.lcd_ch_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current Z position", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"eV", None))
        self.Plot_x_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"ChangeN", None))
        self.Plot_x_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Timestamp", None))

#if QT_CONFIG(tooltip)
        self.ch_pos_left.setToolTip(QCoreApplication.translate("MainWindow", u"Decrease", None))
#endif // QT_CONFIG(tooltip)
        self.ch_pos_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.Step_ch_pos.setToolTip(QCoreApplication.translate("MainWindow", u"Each Step size Z", None))
#endif // QT_CONFIG(tooltip)
        self.Step_ch_pos.setPrefix("")
        self.Step_ch_pos.setSuffix(QCoreApplication.translate("MainWindow", u" eV", None))
#if QT_CONFIG(tooltip)
        self.ch_pos_right.setToolTip(QCoreApplication.translate("MainWindow", u"Increase", None))
#endif // QT_CONFIG(tooltip)
        self.ch_pos_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.Channel_tabs.setTabText(self.Channel_tabs.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Channel", None))
        self.X_position.setTitle(QCoreApplication.translate("MainWindow", u"X_position", None))
        self.Adc_box_3.setTitle(QCoreApplication.translate("MainWindow", u"X_set", None))
#if QT_CONFIG(tooltip)
        self.lcd_X_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"um", None))
        self.X_pos_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.Step_X_pos.setToolTip(QCoreApplication.translate("MainWindow", u"Each Step size X", None))
#endif // QT_CONFIG(tooltip)
        self.Step_X_pos.setSuffix(QCoreApplication.translate("MainWindow", u" um", None))
        self.X_pos_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.Channel_tabs.setTabText(self.Channel_tabs.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Ch3_X", None))
        self.Z_position.setTitle(QCoreApplication.translate("MainWindow", u"Z_position", None))
        self.Adc_box_4.setTitle(QCoreApplication.translate("MainWindow", u"Z_set", None))
#if QT_CONFIG(tooltip)
        self.lcd_Z_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current Z position", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"um", None))
#if QT_CONFIG(tooltip)
        self.Z_pos_left.setToolTip(QCoreApplication.translate("MainWindow", u"Decrease", None))
#endif // QT_CONFIG(tooltip)
        self.Z_pos_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.Step_Z_pos.setToolTip(QCoreApplication.translate("MainWindow", u"Each Step size Z", None))
#endif // QT_CONFIG(tooltip)
        self.Step_Z_pos.setPrefix("")
        self.Step_Z_pos.setSuffix(QCoreApplication.translate("MainWindow", u" um", None))
#if QT_CONFIG(tooltip)
        self.Z_pos_right.setToolTip(QCoreApplication.translate("MainWindow", u"Increase", None))
#endif // QT_CONFIG(tooltip)
        self.Z_pos_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.Channel_tabs.setTabText(self.Channel_tabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Ch5_Z", None))
        self.Msg_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt;&gt;</span></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuInstrument.setTitle(QCoreApplication.translate("MainWindow", u"Instrument", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

