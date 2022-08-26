# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
import sys
import re

import editorUI

import json
import mqtt
from datetime import datetime
import scrape_docs, collections
import pickle

import threading
import configparser
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMessageBox, QTextBrowser, QLabel, QVBoxLayout, QWidget, \
    QPushButton, QTableWidgetItem

config_name = 'tasmoeditor.cfg'                # contains config data
tasmota_cmd_file = 'tasmota_cmds.pkl'

class UI(QtWidgets.QMainWindow, editorUI.Ui_MainWindow):

    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)
        self.config = configparser.ConfigParser()
        if os.path.isfile(config_name):                                                     # load app config file (*.cfg)
            self.config.read(config_name)
        else:
            QMessageBox.warning(self, 'No config file loaded!','Please make sure, that a "tasmohab.cfg" exists and is loaded!')
        self.docs_url = self.config['DEFAULT']['TasmotaDocs']
        self.response_dict = {}                             # stores the responses from tasmota device
        self.tasmota_devices = {}
        self.device_connected = False
        self.current_cmd_topic = ""
        self.current_state_topic = ""
        self.col_prefix = 'Parameter'
        self.header_labels = ['Command', self.col_prefix + '1']
        mqtt.init_mqtt(self)
        self.CmdtableWidget.setColumnCount(2)
        self.CmdtableWidget.setHorizontalHeaderLabels(self.header_labels)
        self.actionClear_tasmota_commands.triggered.connect(self.del_tasmota_cmds_file)
        self.btn_connect_mqtt.clicked.connect(mqtt.connect_mqtt)
        self.btn_disconnect.clicked.connect(mqtt.disconnect_mqtt)
        self.btn_clear_log.clicked.connect(self.clear_log)
        self.btn_show_cmd_docs.clicked.connect(self.show_cmnd_docs)
        self.btn_link_device.clicked.connect(self.link_tasmota_device)
        self.CmdtableWidget.horizontalHeader()
        if os.path.isfile(tasmota_cmd_file):                                         # load tasmota cmd file if exists
            with open(tasmota_cmd_file, 'rb') as f:
                data = pickle.load(f)                                               # load data with pickle
                self.docs_url = tasmota_cmd_file                                     # change url because it was loaded from file
                self.doc_thread_result(data)                                        # save data from file to var and display cmds in ui
        else:                                                                       # fetch cmds from url
            try:
                self.init_scraper(self.docs_url)
            except Exception as e:
                self.append_to_log('Could not get commands list from:'+self.docs_url)
                print(e)

    def append_to_log(self, text):
        self.txt_log.append(datetime.today().strftime('%d-%m-%Y %H:%M:%S') + '\t' + str(text))  # '\t' = tab space
        if len(text) > 50:
            text = text[:150 or None] + ' ...'
        self.lbl_last_log.setText(datetime.today().strftime('%d-%m-%Y %H:%M:%S') + '\t' + str(text))

    def clear_log(self):
        """Clears all log entries"""
        self.txt_log.clear()

    def init_scraper(self, url):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a scrape_worker object
        self.scrape_worker = scrape_page(url)
        # Step 4: Move scrape_worker to the thread
        self.scrape_worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.scrape_worker.run)
        self.scrape_worker.finished.connect(self.thread.quit)
        self.scrape_worker.finished.connect(self.scrape_worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.scrape_worker.result.connect(self.doc_thread_result)
        # Step 6: Start the thread
        self.thread.start()

    def doc_thread_result(self,data):
        self.cmds_in_docs = collections.OrderedDict(sorted(data.items()))
        if not os.path.isfile(tasmota_cmd_file):
            with open(tasmota_cmd_file, 'wb') as f:
                pickle.dump(self.cmds_in_docs, f)
        self.append_to_log('Docs fetched from: '+self.docs_url)
        self.btn_show_cmd_docs.setEnabled(True)
        self.cmd_list_widget.clear()
        for key in self.cmds_in_docs:
            self.cmd_list_widget.addItem(key)
        self.cmd_list_widget.itemClicked.connect(self.listwidgetclicked)

    def listwidgetclicked(self, item):
        #self.CmdtableWidget.clear()
        btn_widgets = self.CmdtableWidget.findChildren(QPushButton)  # returns a list of all QLineEdit objects
        for widget in btn_widgets:  # loop through all found QLineEdit widgets
            widget.setParent(None)
            widget.deleteLater()
        self.CmdtableWidget.setRowCount(0)
        self.CmdtableWidget.setColumnCount(2)
        no_cmnds = len(self.cmds_in_docs[item.text()])
        self.CmdtableWidget.setRowCount(no_cmnds)
        for i, key in enumerate(self.cmds_in_docs[item.text()]):
            btn = QPushButton(key)
            cmd = key.split('/')[0]
            if '<x>' or '<X>' in key:
                cmd = cmd.replace('<x>', '')
            btn.setObjectName(cmd)          # object name is the FIRST command!
            btn.setToolTip('<html>Command:'+key+'<br>'+self.cmds_in_docs[item.text()][key]+'</html>')
            btn.clicked.connect(self.cmd_btnclicked)
            self.CmdtableWidget.setCellWidget(i, 0, btn)
            if cmd in self.response_dict:
                self.draw_data_table(self.response_dict[cmd])           # draw stored data from dict to table

    def cmd_btnclicked(self):
        sender = self.sender()
        cmd = sender.objectName()           # get objectname (=the command) of button
        if '<x>' or '<X>' in cmd:
            cmd = cmd.replace('<x>','')
        try:
            mqtt.client.publish(self.current_cmd_topic + cmd, "")
            self.append_to_log("TX:" + self.current_cmd_topic + cmd)
        except Exception as e:
            self.append_to_log(str(e))
            print(e)

    def draw_data_table(self, payload):
        para_no = 1
        header = self.header_labels
        for key in payload:
            try:
                para_no = int(re.findall(r'\d+', key)[-1])  # search for parameter, i.e. POWER1 -> 1
                cmd = key.replace(str(para_no), "")  # remove parameter from key
            except Exception as e:
                cmd = key
            self.response_dict.setdefault(cmd, {})
            self.response_dict[cmd][key] = payload[key]
            btn_widgets = self.CmdtableWidget.findChildren(QPushButton)  # returns a list of all QLineEdit objects
            for widget in btn_widgets:  # loop through all found QLineEdit widgets
                if str(cmd).lower() == str(widget.objectName()).lower():  # and look if the widget name is in 'json_dev_status' dict
                    #print('Found btn:'+str(widget.objectName()).lower()+' and cmd:'+str(cmd).lower())
                    btn_index = btn_widgets.index(widget)  # get the index of the widget in list
                    no_of_cols = self.CmdtableWidget.columnCount()
                    if no_of_cols - 1 < para_no:
                        self.CmdtableWidget.setColumnCount(no_of_cols + 1)  # expand coloumn count
                        header = header + [self.col_prefix + str(para_no)]  # define header labels
                        self.CmdtableWidget.setHorizontalHeaderLabels(header)  # set new header labels
                    self.header_labels = header  # save header labels in class
                    self.CmdtableWidget.setItem(btn_index, para_no, QTableWidgetItem(json.dumps(payload[key])))  # fill cell with data @ row, col
            self.header_labels = ['Command', self.col_prefix + '1']

    def show_cmnd_docs(self):
        th = '<th style="border:1px solid black;">'
        td = '<td style="border:1px solid black;">'

        html = '<table style="width:100%;text-align:left;">'
        html += '<tr>'+th+'Category</th>'+th+'Command</th>'+th+'Description</th></tr>'

        for cat, val in self.cmds_in_docs.items():
            html += '<tr>'
            html += td + cat + '</td>'
            key = next(iter(val))
            html += td + key + '</td>'
            html += td + val[key] + '</td>'
            html += '</tr>'
            for cmd, desc in val.items():
                if cmd == key:
                    continue
                html += '<tr>'
                html += '<td></td>'
                html += td + cmd + '</td>'
                html += td + desc + '</td>'
                html += '</tr>'
        html += '</table>'
        html = html.replace('\\n', '<br/>').replace('\n', '<br/>')      # replace all newlines with html <br/> tag

        self.det_window = DetailWindow(html, format_to_json=False)                 # initialize detail window
        self.det_window.show()

    def link_tasmota_device(self):
        if self.cmb_devices.currentText() == '':
            QMessageBox.warning(self, 'Select device', 'No Tasmota device connected!')
            return
        sel_device = self.cmb_devices.currentText().split('/')[0]
        topic = self.tasmota_devices[sel_device]        # select choosen device from dict
        self.current_cmd_topic = "cmnd/" + topic + "/"
        self.current_state_topic = "stat/" + topic + "/RESULT"
        if self.device_connected:
            mqtt.client.unsubscribe(self.current_state_topic)
            self.response_dict = {}          # clear dict/ all responses
            self.append_to_log('Unsubscribe topic:' + self.current_state_topic)
            self.cmb_devices.setEnabled(True)
            self.device_connected = False
            self.btn_link_device.setText('Connect to ...')
            self.current_cmd_topic = ""
            self.current_state_topic = ""
            return
        self.append_to_log('Subscribe topic:' + self.current_state_topic)
        mqtt.client.subscribe(self.current_state_topic)
        self.cmb_devices.setEnabled(False)
        self.btn_link_device.setText('Disconnect from ...')
        self.device_connected = True

    def del_tasmota_cmds_file(self):
        try:
            os.remove(tasmota_cmd_file)
            QMessageBox.warning(self, 'Success!','Command file '+tasmota_cmd_file+' deleted. Please restart program.')
        except OSError:
            QMessageBox.information(self, 'Nothing to do!', 'No '+tasmota_cmd_file+' file found.')
            pass


class scrape_page(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(dict)

    def __init__(self, url):
        super(scrape_page, self).__init__()
        self.url = url

    def run(self):
        self.cmds_in_docs = {}
        self.cmds_in_docs = scrape_docs.get_all_commands(self.url)
        self.result.emit(self.cmds_in_docs)
        self.finished.emit()

class DetailWindow(QWidget):
    def __init__(self, string, format_to_json=True):
        super().__init__()
        # global json_dev_status
        layout = QVBoxLayout()
        self.textbrowser = QTextBrowser()
        self.textbrowser.setOpenExternalLinks(True)
        if format_to_json:
            self.textbrowser.append(json.dumps(string, indent=4, sort_keys=False))
        else:
            self.textbrowser.append(string)
        layout.addWidget(self.textbrowser)
        self.setLayout(layout)
        self.setWindowTitle('Details')
        self.setMinimumSize(600, 600)
        self.show()

### MAIN ###
def main_ui():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))
    ui = UI()
    ui.show()
    ui.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))
    sys.exit(app.exec())  # return code of ui app

# this is only for pyinstaller (path for data in --onefile mode)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

## pyrcc5 resource.qrc -o resource_rc.py
## python -m PyQt5.uic.pyuic editorUI.ui -o editorUI.py
if __name__ == '__main__':
    t_ui = threading.Thread(target=main_ui, name='UI_Thread')
    t_ui.start()
    print('Running threads:')
    for thread in threading.enumerate():
        print(thread.name)
    print('\n')

    while not t_ui.is_alive():
        pass
        #time.sleep(.5)
        #if not t_ui.is_alive():
    sys.exit()
