# Form implementation generated from reading ui file 'editorUI.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 883)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.btn_disconnect = QtWidgets.QPushButton(self.groupBox)
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.gridLayout_3.addWidget(self.btn_disconnect, 5, 1, 1, 1)
        self.txt_pass = QtWidgets.QLineEdit(self.groupBox)
        self.txt_pass.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.txt_pass.setObjectName("txt_pass")
        self.gridLayout_3.addWidget(self.txt_pass, 3, 1, 1, 1)
        self.btn_link_device = QtWidgets.QPushButton(self.groupBox)
        self.btn_link_device.setEnabled(False)
        self.btn_link_device.setObjectName("btn_link_device")
        self.gridLayout_3.addWidget(self.btn_link_device, 0, 2, 1, 1)
        self.txt_user = QtWidgets.QLineEdit(self.groupBox)
        self.txt_user.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txt_user.setObjectName("txt_user")
        self.gridLayout_3.addWidget(self.txt_user, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lbl_port = QtWidgets.QLabel(self.groupBox)
        self.lbl_port.setObjectName("lbl_port")
        self.gridLayout_3.addWidget(self.lbl_port, 1, 0, 1, 1)
        self.mqtt_port = QtWidgets.QLineEdit(self.groupBox)
        self.mqtt_port.setMaximumSize(QtCore.QSize(150, 16777215))
        self.mqtt_port.setObjectName("mqtt_port")
        self.gridLayout_3.addWidget(self.mqtt_port, 1, 1, 1, 1)
        self.txt_ip = QtWidgets.QLineEdit(self.groupBox)
        self.txt_ip.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txt_ip.setObjectName("txt_ip")
        self.gridLayout_3.addWidget(self.txt_ip, 0, 1, 1, 1)
        self.cmb_devices = QtWidgets.QComboBox(self.groupBox)
        self.cmb_devices.setEnabled(True)
        self.cmb_devices.setObjectName("cmb_devices")
        self.gridLayout_3.addWidget(self.cmb_devices, 0, 3, 1, 1)
        self.btn_connect_mqtt = QtWidgets.QPushButton(self.groupBox)
        self.btn_connect_mqtt.setEnabled(True)
        self.btn_connect_mqtt.setObjectName("btn_connect_mqtt")
        self.gridLayout_3.addWidget(self.btn_connect_mqtt, 5, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cmd_list_widget = QtWidgets.QListWidget(self.groupBox_4)
        self.cmd_list_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.cmd_list_widget.setMaximumSize(QtCore.QSize(180, 16777215))
        self.cmd_list_widget.setObjectName("cmd_list_widget")
        self.gridLayout_5.addWidget(self.cmd_list_widget, 1, 0, 1, 1)
        self.CmdtableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CmdtableWidget.sizePolicy().hasHeightForWidth())
        self.CmdtableWidget.setSizePolicy(sizePolicy)
        self.CmdtableWidget.setObjectName("CmdtableWidget")
        self.CmdtableWidget.setColumnCount(0)
        self.CmdtableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.CmdtableWidget, 1, 1, 1, 1)
        self.btn_show_cmd_docs = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_show_cmd_docs.setEnabled(False)
        self.btn_show_cmd_docs.setObjectName("btn_show_cmd_docs")
        self.gridLayout_5.addWidget(self.btn_show_cmd_docs, 2, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)
        self.verticalLayout_9.addWidget(self.groupBox_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_log = QtWidgets.QTextBrowser(self.frame_2)
        self.txt_log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txt_log.setObjectName("txt_log")
        self.gridLayout.addWidget(self.txt_log, 1, 0, 1, 1)
        self.btn_clear_log = QtWidgets.QPushButton(self.frame_2)
        self.btn_clear_log.setObjectName("btn_clear_log")
        self.gridLayout.addWidget(self.btn_clear_log, 2, 0, 1, 1)
        self.lbl_log_2 = QtWidgets.QLabel(self.frame_2)
        self.lbl_log_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_log_2.setFont(font)
        self.lbl_log_2.setObjectName("lbl_log_2")
        self.gridLayout.addWidget(self.lbl_log_2, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet(" QProgressBar::chunk\n"
" {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
" }")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_last_log_txt = QtWidgets.QLabel(self.centralwidget)
        self.lbl_last_log_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lbl_last_log_txt.setObjectName("lbl_last_log_txt")
        self.horizontalLayout_3.addWidget(self.lbl_last_log_txt)
        self.lbl_last_log = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_last_log.sizePolicy().hasHeightForWidth())
        self.lbl_last_log.setSizePolicy(sizePolicy)
        self.lbl_last_log.setText("")
        self.lbl_last_log.setObjectName("lbl_last_log")
        self.horizontalLayout_3.addWidget(self.lbl_last_log)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 21))
        self.menubar.setObjectName("menubar")
        self.menuTasmHAB = QtWidgets.QMenu(self.menubar)
        self.menuTasmHAB.setObjectName("menuTasmHAB")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_save_conf = QtGui.QAction(MainWindow)
        self.action_save_conf.setObjectName("action_save_conf")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionLoad_conf = QtGui.QAction(MainWindow)
        self.actionLoad_conf.setObjectName("actionLoad_conf")
        self.actionClear_tasmota_commands = QtGui.QAction(MainWindow)
        self.actionClear_tasmota_commands.setObjectName("actionClear_tasmota_commands")
        self.menuTasmHAB.addSeparator()
        self.menuTasmHAB.addAction(self.actionClear_tasmota_commands)
        self.menuAbout.addAction(self.actionInfo)
        self.menubar.addAction(self.menuTasmHAB.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_ip, self.txt_user)
        MainWindow.setTabOrder(self.txt_user, self.txt_pass)
        MainWindow.setTabOrder(self.txt_pass, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TasmoEditor"))
        self.groupBox.setTitle(_translate("MainWindow", "MQTT Connection"))
        self.label_3.setText(_translate("MainWindow", "MQTT Password"))
        self.label_2.setText(_translate("MainWindow", "MQTT Username"))
        self.btn_disconnect.setText(_translate("MainWindow", "Disconnect from MQTT"))
        self.btn_link_device.setText(_translate("MainWindow", "Connect to ..."))
        self.label.setText(_translate("MainWindow", "MQTT Ip Address"))
        self.lbl_port.setText(_translate("MainWindow", "MQTT Port"))
        self.mqtt_port.setText(_translate("MainWindow", "1883"))
        self.txt_ip.setText(_translate("MainWindow", "192.168.1.100"))
        self.btn_connect_mqtt.setText(_translate("MainWindow", "Connect to MQTT"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Overview"))
        self.btn_show_cmd_docs.setText(_translate("MainWindow", "Show Tasmota commands"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
        self.btn_clear_log.setText(_translate("MainWindow", "Clear Log"))
        self.lbl_log_2.setText(_translate("MainWindow", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Log"))
        self.lbl_last_log_txt.setText(_translate("MainWindow", "Last Log:"))
        self.menuTasmHAB.setTitle(_translate("MainWindow", "Menü"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_save_conf.setText(_translate("MainWindow", "Save Device Config"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionLoad_conf.setText(_translate("MainWindow", "Load Config"))
        self.actionClear_tasmota_commands.setText(_translate("MainWindow", "Clear tasmota commands"))
