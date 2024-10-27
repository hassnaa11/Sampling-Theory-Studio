# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_version2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1464, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Microsoft PhagsPa\";")
        self.title_label.setTextFormat(QtCore.Qt.PlainText)
        self.title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.top_task_bar_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_task_bar_widget.sizePolicy().hasHeightForWidth())
        self.top_task_bar_widget.setSizePolicy(sizePolicy)
        self.top_task_bar_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.top_task_bar_widget.setObjectName("top_task_bar_widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.top_task_bar_widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.original_signal_label = QtWidgets.QLabel(self.top_task_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_signal_label.sizePolicy().hasHeightForWidth())
        self.original_signal_label.setSizePolicy(sizePolicy)
        self.original_signal_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 11pt \"Georgia\";\n"
"")
        self.original_signal_label.setTextFormat(QtCore.Qt.PlainText)
        self.original_signal_label.setObjectName("original_signal_label")
        self.horizontalLayout_10.addWidget(self.original_signal_label)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_13.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(1200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_13)
        self.open_file_button = QtWidgets.QPushButton(self.top_task_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_file_button.sizePolicy().hasHeightForWidth())
        self.open_file_button.setSizePolicy(sizePolicy)
        self.open_file_button.setMinimumSize(QtCore.QSize(100, 30))
        self.open_file_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.open_file_button.setMouseTracking(True)
        self.open_file_button.setStyleSheet("font: italic 10pt \"Georgia\";\n"
"background-color: rgb(169, 222, 216);\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.open_file_button.setObjectName("open_file_button")
        self.horizontalLayout_10.addWidget(self.open_file_button)
        self.mixer_button = QtWidgets.QPushButton(self.top_task_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.mixer_button.sizePolicy().hasHeightForWidth())
        self.mixer_button.setSizePolicy(sizePolicy)
        self.mixer_button.setMinimumSize(QtCore.QSize(80, 30))
        self.mixer_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.mixer_button.setMouseTracking(True)
        self.mixer_button.setStyleSheet("font: italic 10pt \"Georgia\";\n"
"background-color: rgb(169, 222, 216);\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"border-radius: 10px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Desktop/icons/icons8-zoom-out-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.mixer_button.setIcon(icon)
        self.mixer_button.setObjectName("mixer_button")
        self.horizontalLayout_10.addWidget(self.mixer_button)
        self.verticalLayout_2.addWidget(self.top_task_bar_widget, 0, QtCore.Qt.AlignLeft)
        
        ########### original graph ###########

        self.original_signal_graph = pg.PlotWidget(self.centralwidget)
        self.original_signal_graph.setMouseEnabled(x=True, y=True) 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_signal_graph.sizePolicy().hasHeightForWidth())
        
        self.original_signal_graph.setSizePolicy(sizePolicy)
        self.original_signal_graph.setMinimumSize(QtCore.QSize(0, 110))
        self.original_signal_graph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.original_signal_graph.setMouseTracking(True)
        self.original_signal_graph.setTabletTracking(True)
        self.original_signal_graph.setAcceptDrops(True)
        self.original_signal_graph.setAutoFillBackground(False)
        self.original_signal_graph.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"border-radius: 25px;\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"widget-shadow: 2px 2px 5px rgb(0, 0, 0);")
        self.original_signal_graph.setObjectName("original_signal_graph")
        self.verticalLayout_2.addWidget(self.original_signal_graph)


        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.actual_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actual_radioButton.sizePolicy().hasHeightForWidth())
        self.actual_radioButton.setSizePolicy(sizePolicy)
        self.actual_radioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.actual_radioButton.setObjectName("actual_radioButton")
        self.horizontalLayout_5.addWidget(self.actual_radioButton, 0, QtCore.Qt.AlignLeft)
        self.normalized_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalized_radioButton.sizePolicy().hasHeightForWidth())
        self.normalized_radioButton.setSizePolicy(sizePolicy)
        self.normalized_radioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.normalized_radioButton.setObjectName("normalized_radioButton")
        self.horizontalLayout_5.addWidget(self.normalized_radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fs_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_label.sizePolicy().hasHeightForWidth())
        self.fs_label.setSizePolicy(sizePolicy)
        self.fs_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.fs_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.fs_label.setObjectName("fs_label")
        self.horizontalLayout_4.addWidget(self.fs_label)
        self.snr_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snr_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.snr_horizontalSlider.setSizePolicy(sizePolicy)
        self.snr_horizontalSlider.setMinimumSize(QtCore.QSize(80, 0))
        self.snr_horizontalSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.snr_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"        height: 8px;\n"
"        background: #A9DED8;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QSlider::handle:horizontal {\n"
"        background: #498480;\n"
"        border: 2px solid #A9DED8;\n"
"        width: 20px;\n"
"        height: 20px;\n"
"        margin: -6px 0;\n"
"        border-radius: 10px;\n"
"    }\n"
"    QSlider::sub-page:horizontal {\n"
"        background: #498480;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QSlider::add-page:horizontal {\n"
"        background: #A9DED8;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
" QSlider::tick-position:both {\n"
"        height: 12px; /* Make the tick marks taller */\n"
"        width: 3px;   /* Adjust the tick width */\n"
"    }\n"
"\n"
"    QSlider::tick:horizontal {\n"
"        background: white;  /* Make the ticks white */\n"
"    }")
        self.snr_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.snr_horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.snr_horizontalSlider.setObjectName("snr_horizontalSlider")
        self.horizontalLayout_4.addWidget(self.snr_horizontalSlider)
        self.fs_value_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_value_label.sizePolicy().hasHeightForWidth())
        self.fs_value_label.setSizePolicy(sizePolicy)
        self.fs_value_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.fs_value_label.setStyleSheet("  background-color: #1C1C1C;  /* Background color */\n"
"    color: white;  /* Text color */\n"
"    border: 1px solid #1C1C1C;\n"
"    border-radius: 15px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: italic 10pt \"Georgia\";")
        self.fs_value_label.setObjectName("fs_value_label")
        self.horizontalLayout_4.addWidget(self.fs_value_label)
        self.methods_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methods_comboBox.sizePolicy().hasHeightForWidth())
        self.methods_comboBox.setSizePolicy(sizePolicy)
        self.methods_comboBox.setMinimumSize(QtCore.QSize(100, 35))
        self.methods_comboBox.setStyleSheet("QComboBox {\n"
"    background-color: #1C1C1C;  /* Background color */\n"
"    color: white;  /* Text color */\n"
"    border: 1px solid #1C1C1C;\n"
"    border-radius: 15px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: italic 10pt \"Georgia\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    border-radius: 10px;  /* Rounded corners for the arrow box */\n"
"    background-color: #1C1C1C;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    color: white;  /* Arrow color */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #1C1C1C;\n"
"    selection-background-color: #1C1C1C;  /* Selected item background color */\n"
"    background-color: #1C1C1C;  /* Dropdown background color */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.methods_comboBox.setObjectName("methods_comboBox")
        self.methods_comboBox.addItem("")
        self.methods_comboBox.addItem("")
        self.methods_comboBox.addItem("")
        self.methods_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.methods_comboBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.snr_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snr_label.sizePolicy().hasHeightForWidth())
        self.snr_label.setSizePolicy(sizePolicy)
        self.snr_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.snr_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.snr_label.setObjectName("snr_label")
        self.horizontalLayout_4.addWidget(self.snr_label)
        self.fs_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fs_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.fs_horizontalSlider.setSizePolicy(sizePolicy)
        self.fs_horizontalSlider.setMinimumSize(QtCore.QSize(80, 0))
        self.fs_horizontalSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.fs_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"        height: 8px;\n"
"        background: #A9DED8;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QSlider::handle:horizontal {\n"
"        background: #498480;\n"
"        border: 2px solid #A9DED8;\n"
"        width: 20px;\n"
"        height: 20px;\n"
"        margin: -6px 0;\n"
"        border-radius: 10px;\n"
"    }\n"
"    QSlider::sub-page:horizontal {\n"
"        background: #498480;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QSlider::add-page:horizontal {\n"
"        background: #A9DED8;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
" QSlider::tick-position:both {\n"
"        height: 12px; /* Make the tick marks taller */\n"
"        width: 3px;   /* Adjust the tick width */\n"
"    }\n"
"\n"
"    QSlider::tick:horizontal {\n"
"        background: white;  /* Make the ticks white */\n"
"    }")
        self.fs_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fs_horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.fs_horizontalSlider.setObjectName("fs_horizontalSlider")
        self.horizontalLayout_4.addWidget(self.fs_horizontalSlider)
        self.snr_value_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snr_value_label.sizePolicy().hasHeightForWidth())
        self.snr_value_label.setSizePolicy(sizePolicy)
        self.snr_value_label.setMaximumSize(QtCore.QSize(140, 16777215))
        self.snr_value_label.setStyleSheet("  background-color: #1C1C1C;  /* Background color */\n"
"    color: white;  /* Text color */\n"
"    border: 1px solid #1C1C1C;\n"
"    border-radius: 15px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: italic 10pt \"Georgia\";")
        self.snr_value_label.setObjectName("snr_value_label")
        self.horizontalLayout_4.addWidget(self.snr_value_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        
        ########### reconstructed graph ###########
        self.reconstructed_signal_label = QtWidgets.QLabel(self.centralwidget)
       
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reconstructed_signal_label.sizePolicy().hasHeightForWidth())
        self.reconstructed_signal_label.setSizePolicy(sizePolicy)
        self.reconstructed_signal_label.setMinimumSize(QtCore.QSize(0, 30))
        self.reconstructed_signal_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
         
        self.reconstructed_signal_label.setObjectName("reconstructed_signal_label")
        self.verticalLayout_2.addWidget(self.reconstructed_signal_label)
        
        
        self.reconstructed_signal_graph = pg.PlotWidget(self.centralwidget)
        self.reconstructed_signal_graph.setMouseEnabled(x=True, y=True)
        
        # # self.reconstructed_signal_graph = QtWidgets.QWidget(self.centralwidget)
        # self.reconstructed_signal_graph.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reconstructed_signal_graph.sizePolicy().hasHeightForWidth())
        self.reconstructed_signal_graph.setSizePolicy(sizePolicy)
        self.reconstructed_signal_graph.setMinimumSize(QtCore.QSize(0, 110))
        self.reconstructed_signal_graph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reconstructed_signal_graph.setMouseTracking(True)
        self.reconstructed_signal_graph.setTabletTracking(True)
        self.reconstructed_signal_graph.setAcceptDrops(True)
        self.reconstructed_signal_graph.setAutoFillBackground(False)
        self.reconstructed_signal_graph.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"border-radius: 25px;\n"
"button-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"widget-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"padding-right: 5px;\n"
"padding-left: 5px;")
        self.reconstructed_signal_graph.setObjectName("reconstructed_signal_graph")
        self.verticalLayout_2.addWidget(self.reconstructed_signal_graph)


        self.error_frequency_toggle_button = QtWidgets.QRadioButton(self.centralwidget)
        self.error_frequency_toggle_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.error_frequency_toggle_button.setObjectName("error_frequency_toggle_button")
        self.verticalLayout_2.addWidget(self.error_frequency_toggle_button)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("QStackedWidget{\n"
"            margin: 0px;\n"
"            padding: 0px;\n"
"            border: none;\n"
"}\n"
"\n"
"QWidget{\n"
"        margin: 0px;\n"
"        padding: opx;\n"
"        borer: none;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.difference_signal_label = QtWidgets.QLabel(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difference_signal_label.sizePolicy().hasHeightForWidth())
        self.difference_signal_label.setSizePolicy(sizePolicy)
        self.difference_signal_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 11pt \"Georgia\";\n"
"")
        self.difference_signal_label.setTextFormat(QtCore.Qt.PlainText)
        self.difference_signal_label.setObjectName("difference_signal_label")
        self.verticalLayout_7.addWidget(self.difference_signal_label)
        
        ######## difference signal graph ########

        self.difference_signal_graph = pg.PlotWidget(self.centralwidget)
        self.difference_signal_graph.setMouseEnabled(x=True, y=True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difference_signal_graph.sizePolicy().hasHeightForWidth())
        self.difference_signal_graph.setSizePolicy(sizePolicy)
        self.difference_signal_graph.setMinimumSize(QtCore.QSize(0, 110))
        self.difference_signal_graph.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"border-radius: 25px;\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"widget-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"")
        self.difference_signal_graph.setObjectName("difference_signal_graph")
        self.verticalLayout_7.addWidget(self.difference_signal_graph)
        self.stackedWidget.addWidget(self.page_4)


        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frequancy_domain_label = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequancy_domain_label.sizePolicy().hasHeightForWidth())
        self.frequancy_domain_label.setSizePolicy(sizePolicy)
        self.frequancy_domain_label.setMinimumSize(QtCore.QSize(0, 30))
        self.frequancy_domain_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.frequancy_domain_label.setObjectName("frequancy_domain_label")
        self.verticalLayout_5.addWidget(self.frequancy_domain_label)

        ######## frequency domain graph ########

        self.frequancy_domain_graph = pg.PlotWidget(self.centralwidget)
        self.frequancy_domain_graph.setMouseEnabled(x=True, y=True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequancy_domain_graph.sizePolicy().hasHeightForWidth())
        self.frequancy_domain_graph.setSizePolicy(sizePolicy)
        self.frequancy_domain_graph.setMinimumSize(QtCore.QSize(0, 120))
        self.frequancy_domain_graph.setBaseSize(QtCore.QSize(1100, 110))
        self.frequancy_domain_graph.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"border-radius: 25px;\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"widget-shadow: 2px 2px 5px rgb(0, 0, 0);")
        self.frequancy_domain_graph.setObjectName("frequancy_domain_graph")
        self.verticalLayout_5.addWidget(self.frequancy_domain_graph)
        self.stackedWidget.addWidget(self.page_3)


        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        ########### side bar ###########

        self.side_bar_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_bar_widget.sizePolicy().hasHeightForWidth())
        self.side_bar_widget.setSizePolicy(sizePolicy)
        self.side_bar_widget.setObjectName("side_bar_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.side_bar_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mixer_label = QtWidgets.QLabel(self.side_bar_widget)
        self.mixer_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 11pt \"Georgia\";\n"
"")
        self.mixer_label.setObjectName("mixer_label")
        self.horizontalLayout_8.addWidget(self.mixer_label)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_20)
        self.tests_comboBox = QtWidgets.QComboBox(self.side_bar_widget)
        self.tests_comboBox.setStyleSheet("QComboBox {\n"
"    background-color: #1C1C1C;  /* Background color */\n"
"    color: white;  /* Text color */\n"
"    border: 1px solid #1C1C1C;\n"
"    border-radius: 15px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: italic 10pt \"Georgia\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    border-radius: 10px;  /* Rounded corners for the arrow box */\n"
"    background-color: #1C1C1C;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    color: white;  /* Arrow color */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #1C1C1C;\n"
"    selection-background-color: #1C1C1C;  /* Selected item background color */\n"
"    background-color: #1C1C1C;  /* Dropdown background color */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.tests_comboBox.setObjectName("tests_comboBox")
        self.tests_comboBox.addItem("")
        self.tests_comboBox.addItem("")
        self.tests_comboBox.addItem("")
        self.tests_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.tests_comboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.side_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setStyleSheet("QTabelWidget {\n"
"    background-color: rgb(0, 0, 0);\n"
"    background-color : back;\n"
"    color: rgb(255, 255, 255);\n"
"    border : none;\n"
"    font-family: \"Arial\";\n"
"    font-size : 14px;\n"
"}\n"
"\n"
"QTabelWidget :: item {\n"
"borde-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QTabelWidget :: item : selected {\n"
"background-color : darckgray;\n"
"}\n"
"\n"
"QHeaderView :: section{\n"
"border : none\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.mixed_signal_label = QtWidgets.QLabel(self.side_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.mixed_signal_label.sizePolicy().hasHeightForWidth())
        self.mixed_signal_label.setSizePolicy(sizePolicy)
        self.mixed_signal_label.setMinimumSize(QtCore.QSize(150, 30))
        self.mixed_signal_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 10pt \"Georgia\";\n"
"")
        self.mixed_signal_label.setObjectName("mixed_signal_label")
        self.verticalLayout_6.addWidget(self.mixed_signal_label)
        self.mixed_signal_graph = pg.PlotWidget(self.centralwidget)
        self.mixed_signal_graph.setMouseEnabled(x=True, y=True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mixed_signal_graph.sizePolicy().hasHeightForWidth())
        self.mixed_signal_graph.setSizePolicy(sizePolicy)
        self.mixed_signal_graph.setMinimumSize(QtCore.QSize(0, 110))
        self.mixed_signal_graph.setMaximumSize(QtCore.QSize(16777215, 600))
        self.mixed_signal_graph.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"border-radius: 25px;\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"widget-shadow: 2px 2px 5px rgb(0, 0, 0);")
        self.mixed_signal_graph.setObjectName("mixed_signal_graph")
        self.verticalLayout_6.addWidget(self.mixed_signal_graph)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_19)
        self.apply_button_2 = QtWidgets.QPushButton(self.side_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(90)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button_2.sizePolicy().hasHeightForWidth())
        self.apply_button_2.setSizePolicy(sizePolicy)
        self.apply_button_2.setMinimumSize(QtCore.QSize(80, 30))
        self.apply_button_2.setStyleSheet("font: italic 10pt \"Georgia\";\n"
"background-color: rgb(169, 222, 216);\n"
"buttoon-shadow: 2px 2px 5px rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.apply_button_2.setObjectName("apply_button_2")
        self.horizontalLayout_9.addWidget(self.apply_button_2)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_18)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_2.addWidget(self.side_bar_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Sampling Theory Studio"))
        self.original_signal_label.setText(_translate("MainWindow", "Original Signal"))
        self.open_file_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.open_file_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">)pen</span></p></body></html>"))
        self.open_file_button.setText(_translate("MainWindow", "Open File"))
        self.mixer_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.mixer_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">)pen</span></p></body></html>"))
        self.mixer_button.setText(_translate("MainWindow", "Mixer"))
        self.actual_radioButton.setText(_translate("MainWindow", "Actual"))
        self.normalized_radioButton.setText(_translate("MainWindow", "Normalized"))
        self.fs_label.setText(_translate("MainWindow", "FS"))
        self.fs_value_label.setText(_translate("MainWindow", "FS: "))
        self.methods_comboBox.setItemText(0, _translate("MainWindow", "Method"))
        self.methods_comboBox.setItemText(1, _translate("MainWindow", "Method1"))
        self.methods_comboBox.setItemText(2, _translate("MainWindow", "Method2"))
        self.methods_comboBox.setItemText(3, _translate("MainWindow", "Method3"))
        self.snr_label.setText(_translate("MainWindow", "SNR"))
        self.snr_value_label.setText(_translate("MainWindow", "SNR: "))
        self.reconstructed_signal_label.setText(_translate("MainWindow", "Reconstructed Signal"))
        self.error_frequency_toggle_button.setText(_translate("MainWindow", "Show Error Difference"))
        self.difference_signal_label.setText(_translate("MainWindow", "Difference Signal"))
        self.frequancy_domain_label.setText(_translate("MainWindow", "Frequency Domain"))
        self.mixer_label.setText(_translate("MainWindow", "Mixer"))
        self.tests_comboBox.setItemText(0, _translate("MainWindow", "Tests"))
        self.tests_comboBox.setItemText(1, _translate("MainWindow", "Testcase1"))
        self.tests_comboBox.setItemText(2, _translate("MainWindow", "Testcase2"))
        self.tests_comboBox.setItemText(3, _translate("MainWindow", "Testcase3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "frequency"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "amplitude"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "phase"))
        self.mixed_signal_label.setText(_translate("MainWindow", "Mixed Signal"))
        self.apply_button_2.setText(_translate("MainWindow", "Apply"))