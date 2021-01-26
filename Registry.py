# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from copy import copy

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from winreg import *
import sys

from PyQt5.QtWidgets import QWidget, QTableWidget, QListWidget, QListWidgetItem, QMessageBox, QFileSystemModel, \
    QTreeView, QVBoxLayout
import os, sys, shutil, json, time, io
import re

from notebook.transutils import base_dir

varSubkey1 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
varSubkey2 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Runonce"
varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
varReg2 = ConnectRegistry(None, HKEY_CURRENT_USER)
varKey1 = OpenKey(varReg1, varSubkey1)
varKey2 = OpenKey(varReg1, varSubkey2)
varKey3 = OpenKey(varReg2, varSubkey1)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Registry")
        MainWindow.resize(1053, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(320, 90, 711, 501))
        self.listView.setObjectName("listView")

        self.listView1 = QtWidgets.QListWidget(self.centralwidget)
        self.listView1.setGeometry(QtCore.QRect(20, 600, 1011, 81))
        self.listView1.setObjectName("listWidget")

        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 90, 400, 600))
        self.model = QFileSystemModel()
        path = ""
        self.model.setRootPath('')
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setAnimated(False)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)
        self.treeView.setWindowTitle("Dir View")
        self.treeView.resize(291, 501)
        self.treeView.setObjectName("treeView")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 50, 711, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Search...')


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QMenu(self.menu)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.actionb = QtWidgets.QAction(MainWindow)
        self.actionb.setObjectName("actionb")
        self.actionc = QtWidgets.QAction(MainWindow)
        self.actionc.setObjectName("actionc")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.action.addAction(self.actiona)
        self.action.addAction(self.actionb)
        self.action.addAction(self.actionc)
        self.action.addAction(self.actiond)
        self.menu.addAction(self.action.menuAction())
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Registry_Window_start(self):
        rootkey = []
        varSubkey1 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        varSubkey2 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Runonce"
        varSubkey3 = "SOFTWARE\Classes\exefile\shell\open\command"
        varSubkey4 = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varReg2 = ConnectRegistry(None, HKEY_CURRENT_USER)

        varKey1 = OpenKey(varReg1, varSubkey1)
        varKey2 = OpenKey(varReg1, varSubkey2)
        varKey3 = OpenKey(varReg2, varSubkey1)
        varKey4 = OpenKey(varReg1, varSubkey3)
        varKey5 = OpenKey(varReg1, varSubkey4)

        for i in range(1024):
            try:
                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append(keyValue1 + ": " + dataValue1)

            except:
                pass

            try:
                (keyValue2, dataValue2, typeValue2) = EnumValue(varKey2, i)

                rootkey.append(keyValue2 + ": " + dataValue2)

            except:
                pass

            try:
                (keyValue3, dataValue3, typeValue3) = EnumValue(varKey3, i)

                rootkey.append(keyValue3 + ": " + dataValue3)

            except:
                pass

            try:
                (keyValue4, dataValue4, typeValue4) = EnumValue(varKey4, i)

                rootkey.append(keyValue4 + ": " + dataValue4)

            except:
                pass

            try:
                (keyValue5, dataValue5, typeValue5) = EnumValue(varKey5, i)

                rootkey.append(keyValue5 + ": " + dataValue5)

            except:
                pass
        self.listView.clear()
        if not rootkey:
            RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item2 = QListWidgetItem()
            item2.setText(RegTime + " 레지스트리 데이터 값이 존재 하지 않습니다.")
            self.listView1.addItem(item2)
        else:
            self.listView.clear()
            for i in range(len(rootkey)):
                item = QListWidgetItem()
                item.setText(rootkey[i])
                self.listView.addItem(item)

    def Hidden_malware(self):
        rootkey = []
        varSubkey1 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varKey1 = OpenKey(varReg1, varSubkey1)

        for i in range(1024):
            try:
                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append(keyValue1 + ": " + dataValue1)

            except:
                pass
        print(len(rootkey))
        self.listView.clear()
        if not rootkey:
            RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item2 = QListWidgetItem()
            item2.setText(RegTime + " 레지스트리 데이터 값이 존재 하지 않습니다.")
            self.listView1.addItem(item2)
        else:

            for i in range(len(rootkey)):
                item = QListWidgetItem()
                item.setText(rootkey[i])
                self.listView.addItem(item)


    def Add_execute(self):
        rootkey = []
        varSubkey1 = r"exefile\shell\open\command"
        varSubkey2 = r"comfile\shell\open\command"
        varSubkey3 = r"batfile\shell\open\command"
        varSubkey4 = r"htafile\shell\open\command"
        varSubkey5 = r"piffile\shell\open\command"
        varSubkey6 = r"SOFTWARE\CLASSES\batfile\shell\open\command"
        varSubkey7 = r"SOFTWARE\CLASSES\comfile\shell\open\command"
        varSubkey8 = r"SOFTWARE\CLASSES\exefile\shell\open\command"
        varSubkey9 = r"SOFTWARE\CLASSES\htafile\shell\open\command"
        varSubkey10 = r"SOFTWARE\CLASSES\piffile\shell\open\command"
        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varReg2 = ConnectRegistry(None, HKEY_CLASSES_ROOT)
        varKey1 = OpenKey(varReg2, varSubkey1)
        varKey2 = OpenKey(varReg2, varSubkey2)
        varKey3 = OpenKey(varReg2, varSubkey3)
        varKey4 = OpenKey(varReg2, varSubkey4)
        varKey5 = OpenKey(varReg2, varSubkey5)
        varKey6 = OpenKey(varReg1, varSubkey6)
        varKey7 = OpenKey(varReg1, varSubkey7)
        varKey8 = OpenKey(varReg1, varSubkey8)
        varKey9 = OpenKey(varReg1, varSubkey9)
        varKey10 = OpenKey(varReg1, varSubkey10)

        for i in range(1024):
            try:

                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append("HKCR_exfile " + keyValue1 + ": " + dataValue1)

            except:
                pass

            try:
                (keyValue2, dataValue2, typeValue2) = EnumValue(varKey2, i)

                rootkey.append("HKCR_comfile " + keyValue2 + ": " + dataValue2)

            except:
                pass

            try:
                (keyValue3, dataValue3, typeValue3) = EnumValue(varKey3, i)

                rootkey.append("HKCR_batfile " + keyValue3 + ": " + dataValue3)

            except:
                pass

            try:
                (keyValue4, dataValue4, typeValue4) = EnumValue(varKey4, i)

                rootkey.append("HKCR_htafile " + keyValue4 + ": " + dataValue4)

            except:
                pass

            try:
                (keyValue5, dataValue5, typeValue5) = EnumValue(varKey5, i)

                rootkey.append("HKCR_piffile " + keyValue5 + ": " + dataValue5)

            except:
                pass

            try:
                (keyValue6, dataValue6, typeValue6) = EnumValue(varKey6, i)

                rootkey.append("HKLM_batfile " + keyValue6 + ": " + dataValue6)

            except:
                pass

            try:
                (keyValue7, dataValue7, typeValue7) = EnumValue(varKey7, i)

                rootkey.append("HKLM_comfile " + keyValue7 + ": " + dataValue7)

            except:
                pass

            try:
                (keyValue8, dataValue8, typeValue8) = EnumValue(varKey8, i)

                rootkey.append("HKLM_exefile " + keyValue8 + ": " + dataValue8)

            except:
                pass

            try:
                (keyValue9, dataValue9, typeValue9) = EnumValue(varKey9, i)

                rootkey.append("HKLM_htafile " + keyValue9 + ": " + dataValue9)

            except:
                pass

            try:
                (keyValue10, dataValue10, typeValue10) = EnumValue(varKey10, i)

                rootkey.append("HKLM_piffile " + keyValue10 + ": " + dataValue10)

            except:
                pass
        print(len(rootkey))
        self.listView.clear()
        if not rootkey:
            RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item2 = QListWidgetItem()
            item2.setText(RegTime + " 레지스트리 데이터 값이 존재 하지 않습니다.")
            self.listView1.addItem(item2)
        else:

            for i in range(len(rootkey)):
                item = QListWidgetItem()
                item.setText(rootkey[i])
                self.listView.addItem(item)

    def IE(self):
        rootkey = []
        varSubkey1 = r"Software\Microsoft\Internet Explorer\Main"
        varSubkey2 = r"Software\Microsoft\Internet Explorer\Toolbar"

        varSubkey4 = r"SOFTWARE\Microsoft\Internet Explorer\SearchURL"
        varSubkey5 = r"Software\Microsoft\Internet Explorer\URLSearchHooks"

        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varReg2 = ConnectRegistry(None, HKEY_CURRENT_USER)
        varKey1 = OpenKey(varReg2, varSubkey1)
        varKey2 = OpenKey(varReg2, varSubkey2)

        varKey4 = OpenKey(varReg1, varSubkey4)
        varKey5 = OpenKey(varReg2, varSubkey5)

        for i in range(1024):
            try:

                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append("HKCU_Main " + keyValue1 + ": " + dataValue1)

            except:
                pass

            try:
                (keyValue2, dataValue2, typeValue2) = EnumValue(varKey2, i)

                rootkey.append("HKCU_Toolbar " + keyValue2 + ": " + dataValue2)

            except:
                pass


            try:
                (keyValue4, dataValue4, typeValue4) = EnumValue(varKey4, i)

                rootkey.append("HKLM_SearchURL " + keyValue4 + ": " + dataValue4)

            except:
                pass

            try:
                (keyValue5, dataValue5, typeValue5) = EnumValue(varKey5, i)

                rootkey.append("Default URL Searchhook " + keyValue5 + ": " + dataValue5)

            except:
                pass

        print(len(rootkey))
        self.listView.clear()
        if not rootkey:
            RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item2 = QListWidgetItem()
            item2.setText(RegTime + " 레지스트리 데이터 값이 존재 하지 않습니다.")
            self.listView1.addItem(item2)
        else:

            for i in range(len(rootkey)):
                item = QListWidgetItem()
                item.setText(rootkey[i])
                self.listView.addItem(item)

    def backup_start_window(self):
        if os.path.exists('C:\\Users\\backup') == False:
            os.mkdir('C:\\Users\\backup')
            if os.path.exists('C:\\Users\\backup\\start') == False:
                os.mkdir('C:\\Users\\backup\\start')
        else:
            if os.path.exists('C:\\Users\\backup\\start') == False:
                os.mkdir('C:\\Users\\backup\\start')

        filepath = 'C:\\Users\\backup\\start\\'
        filename = time.strftime('%Y-%m-%d_%H.%M.%SStart', time.localtime(time.time()))
        filename = re.sub("[\/*?\"<>|]", "", filename)
        f = open(filepath + filename + '.txt', 'w')

        rootkey = []
        varSubkey1 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        varSubkey2 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Runonce"
        varSubkey3 = "SOFTWARE\Classes\exefile\shell\open\command"
        varSubkey4 = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varReg2 = ConnectRegistry(None, HKEY_CURRENT_USER)

        varKey1 = OpenKey(varReg1, varSubkey1)
        varKey2 = OpenKey(varReg1, varSubkey2)
        varKey3 = OpenKey(varReg2, varSubkey1)
        varKey4 = OpenKey(varReg1, varSubkey3)
        varKey5 = OpenKey(varReg1, varSubkey4)

        for i in range(1024):
            try:
                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append(keyValue1 + ": " + dataValue1)

            except:
                pass

            try:
                (keyValue2, dataValue2, typeValue2) = EnumValue(varKey2, i)

                rootkey.append(keyValue2 + ": " + dataValue2)

            except:
                pass

            try:
                (keyValue3, dataValue3, typeValue3) = EnumValue(varKey3, i)

                rootkey.append(keyValue3 + ": " + dataValue3)

            except:
                pass

            try:
                (keyValue4, dataValue4, typeValue4) = EnumValue(varKey4, i)

                rootkey.append(keyValue4 + ": " + dataValue4)

            except:
                pass

            try:
                (keyValue5, dataValue5, typeValue5) = EnumValue(varKey5, i)

                rootkey.append(keyValue5 + ": " + dataValue5)
                for j in range(len(rootkey)):
                    f.write(rootkey[j] + '\n')
            except:
                pass
        f.close()
        RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        item2 = QListWidgetItem()
        item2.setText(RegTime + " 백업 파일 생성")
        self.listView1.addItem(item2)

    def backup_hidden(self):
        if os.path.exists('C:\\Users\\backup') == False:
            os.mkdir('C:\\Users\\backup')
            if os.path.exists('C:\\Users\\backup\\hidden') == False:
                os.mkdir('C:\\Users\\backup\\hidden')
        else:
            if os.path.exists('C:\\Users\\backup\\hidden') == False:
                os.mkdir('C:\\Users\\backup\\hidden')

        filepath = 'C:\\Users\\backup\\hidden'
        filename = time.strftime('%Y-%m-%d_%H.%M.%SHidden', time.localtime(time.time()))
        filename = re.sub("[\/*?\"<>|]", "", filename)
        f = open(filepath + filename + '.txt', 'w')
        rootkey = []
        varSubkey1 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varKey1 = OpenKey(varReg1, varSubkey1)

        for i in range(1024):
            try:
                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append(keyValue1 + ": " + dataValue1)
                for k in range(len(rootkey)):
                    f.write(rootkey[k])

            except:
                pass

        f.close()

    def backup_add(self):
        if os.path.exists('C:\\Users\\backup') == False:
            os.mkdir('C:\\Users\\backup')
            if os.path.exists('C:\\Users\\backup\\add') == False:
                os.mkdir('C:\\Users\\backup\\add')
        else:
            if os.path.exists('C:\\Users\\backup\\add') == False:
                os.mkdir('C:\\Users\\backup\\add')

        filepath = 'C:\\Users\\backup\\add\\'
        filename = time.strftime('%Y-%m-%d_%H.%M.%SAdd', time.localtime(time.time()))
        filename = re.sub("[\/*?\"<>|]", "", filename)
        f = open(filepath + filename + '.txt', 'w')

        rootkey = []
        varSubkey1 = r"exefile\shell\open\command"
        varSubkey2 = r"comfile\shell\open\command"
        varSubkey3 = r"batfile\shell\open\command"
        varSubkey4 = r"htafile\shell\open\command"
        varSubkey5 = r"piffile\shell\open\command"
        varSubkey6 = r"SOFTWARE\CLASSES\batfile\shell\open\command"
        varSubkey7 = r"SOFTWARE\CLASSES\comfile\shell\open\command"
        varSubkey8 = r"SOFTWARE\CLASSES\exefile\shell\open\command"
        varSubkey9 = r"SOFTWARE\CLASSES\htafile\shell\open\command"
        varSubkey10 = r"SOFTWARE\CLASSES\piffile\shell\open\command"
        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varReg2 = ConnectRegistry(None, HKEY_CLASSES_ROOT)
        varKey1 = OpenKey(varReg2, varSubkey1)
        varKey2 = OpenKey(varReg2, varSubkey2)
        varKey3 = OpenKey(varReg2, varSubkey3)
        varKey4 = OpenKey(varReg2, varSubkey4)
        varKey5 = OpenKey(varReg2, varSubkey5)
        varKey6 = OpenKey(varReg1, varSubkey6)
        varKey7 = OpenKey(varReg1, varSubkey7)
        varKey8 = OpenKey(varReg1, varSubkey8)
        varKey9 = OpenKey(varReg1, varSubkey9)
        varKey10 = OpenKey(varReg1, varSubkey10)

        for i in range(1024):
            try:

                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append("HKCR_exfile " + keyValue1 + ": " + dataValue1)

            except:
                pass

            try:
                (keyValue2, dataValue2, typeValue2) = EnumValue(varKey2, i)

                rootkey.append("HKCR_comfile " + keyValue2 + ": " + dataValue2)

            except:
                pass

            try:
                (keyValue3, dataValue3, typeValue3) = EnumValue(varKey3, i)

                rootkey.append("HKCR_batfile " + keyValue3 + ": " + dataValue3)

            except:
                pass

            try:
                (keyValue4, dataValue4, typeValue4) = EnumValue(varKey4, i)

                rootkey.append("HKCR_htafile " + keyValue4 + ": " + dataValue4)

            except:
                pass

            try:
                (keyValue5, dataValue5, typeValue5) = EnumValue(varKey5, i)

                rootkey.append("HKCR_piffile " + keyValue5 + ": " + dataValue5)

            except:
                pass

            try:
                (keyValue6, dataValue6, typeValue6) = EnumValue(varKey6, i)

                rootkey.append("HKLM_batfile " + keyValue6 + ": " + dataValue6)

            except:
                pass

            try:
                (keyValue7, dataValue7, typeValue7) = EnumValue(varKey7, i)

                rootkey.append("HKLM_comfile " + keyValue7 + ": " + dataValue7)

            except:
                pass

            try:
                (keyValue8, dataValue8, typeValue8) = EnumValue(varKey8, i)

                rootkey.append("HKLM_exefile " + keyValue8 + ": " + dataValue8)

            except:
                pass

            try:
                (keyValue9, dataValue9, typeValue9) = EnumValue(varKey9, i)

                rootkey.append("HKLM_htafile " + keyValue9 + ": " + dataValue9)

            except:
                pass

            try:
                (keyValue10, dataValue10, typeValue10) = EnumValue(varKey10, i)

                rootkey.append("HKLM_piffile " + keyValue10 + ": " + dataValue10)
                for l in range(len(rootkey)):
                    f.write(rootkey[l] + '\n')

            except:
                pass

        f.close()
        RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        item2 = QListWidgetItem()
        item2.setText(RegTime + " 백업 파일 생성")
        self.listView1.addItem(item2)

    def backup_IE(self):
        if os.path.exists('C:\\Users\\backup') == False:
            os.mkdir('C:\\Users\\backup')
            if os.path.exists('C:\\Users\\backup\\IE') == False:
                os.mkdir('C:\\Users\\backup\\IE')
        else:
            if os.path.exists('C:\\Users\\backup\\IE') == False:
                os.mkdir('C:\\Users\\backup\\IE')

        filepath = 'C:\\Users\\backup\\IE\\'
        filename = time.strftime('%Y-%m-%d_%H.%M.%SAdd', time.localtime(time.time()))
        filename = re.sub("[\/*?\"<>|]", "", filename)
        f = open(filepath + filename + '.txt', 'w')
        rootkey = []
        varSubkey1 = r"Software\Microsoft\Internet Explorer\Main"
        varSubkey2 = r"Software\Microsoft\Internet Explorer\Toolbar"
        varSubkey3 = r"SOFTWARE\Microsoft\Internet Explorer\SearchURL"
        varSubkey4 = r"Software\Microsoft\Internet Explorer\URLSearchHooks"

        varReg1 = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        varReg2 = ConnectRegistry(None, HKEY_CURRENT_USER)
        varKey1 = OpenKey(varReg2, varSubkey1)
        varKey2 = OpenKey(varReg2, varSubkey2)
        varKey3 = OpenKey(varReg1, varSubkey3)
        varKey4 = OpenKey(varReg2, varSubkey4)

        for i in range(1024):
            try:

                (keyValue1, dataValue1, typeValue1) = EnumValue(varKey1, i)

                rootkey.append("HKCU_Main " + keyValue1 + ": " + dataValue1)

            except:
                pass

            try:
                (keyValue2, dataValue2, typeValue2) = EnumValue(varKey2, i)

                rootkey.append("HKCU_Toolbar " + keyValue2 + ": " + dataValue2)

            except:
                pass

            try:
                (keyValue3, dataValue3, typeValue3) = EnumValue(varKey3, i)

                rootkey.append("HKLM_SearchURL " + keyValue3 + ": " + dataValue3)

            except:
                pass

            try:
                (keyValue4, dataValue4, typeValue4) = EnumValue(varKey4, i)

                rootkey.append("Default URL Searchhook " + keyValue4 + ": " + dataValue4)
            except:
                pass
        for l in range(len(rootkey)):
            f.write(rootkey[l] + '\n')
        f.close()
        RegTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        item2 = QListWidgetItem()
        item2.setText(RegTime + " 백업 파일 생성")
        self.listView1.addItem(item2)

    def exit(self):
        exit();

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("열기")
        delete = menu.addAction("삭제")
        open.triggered.connect(self.open_file)
        delete.triggered.connect(self.delete_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self, event):
        index = self.treeView.currentIndex()
        file_name = self.model.filePath(index)
        os.startfile(file_name)

    def delete_file(self):
        index = self.treeView.currentIndex()
        file_name = self.model.filePath(index)
        os.remove(file_name)

    def on_text_change(self, text):
        for row in range(self.listView.count()):
            it = self.listView.item(row)
            if text:
                it.setHidden(not self.text_filter(text, it.text()))
            else:
                it.setHidden(False)

    def text_filter(self, text, keywords):
        return text.lower() in keywords.lower()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registry"))
        self.menu.setTitle(_translate("MainWindow", "파일"))
        self.menu_2.setTitle(_translate("MainWindow", "보기"))
        self.action.setTitle(_translate("MainWindow", "악성 레지스트리 검사"))
        self.action_2.setText(_translate("MainWindow", "끝내기"))
        self.actiona.setText(_translate("MainWindow", "윈도우 시작시 실행 레지스트리"))
        self.actionb.setText(_translate("MainWindow", "은닉 악성코드 레지스트리"))
        self.actionc.setText(_translate("MainWindow", "추가 실행 레지스트리"))
        self.actiond.setText(_translate("MainWindow", "IE 관련 레지스트리"))
        self.actiona.triggered.connect(self.backup_start_window)
        self.actiona.triggered.connect(self.Registry_Window_start)
        self.actionb.triggered.connect(self.Hidden_malware)
        self.actionc.triggered.connect(self.Add_execute)
        self.actiond.triggered.connect(self.IE)
        self.actionc.triggered.connect(self.backup_add)
        self.actiond.triggered.connect(self.backup_IE)
        self.action_2.triggered.connect(self.exit)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.lineEdit.textChanged.connect(self.on_text_change)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
