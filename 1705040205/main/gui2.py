# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog, QApplication,QHBoxLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 749)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 1121, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_1)
        self.tabWidget_2.setGeometry(QtCore.QRect(210, 0, 911, 611))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1011, 571))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_4)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 901, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 0, 61, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(840, 0, 61, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_1 = QtWidgets.QFrame(self.page)
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout.addWidget(self.frame_1)
        self.stackedWidget.addWidget(self.page)
        self.browser = QWebEngineView(self.stackedWidget)
        self.browser.load(
            QUrl("file:///E:/code/python/inflight_project/client.html"))
        hboxlayout = QHBoxLayout(self.frame_1)
        hboxlayout.addWidget(self.browser)


        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_1 = QtWidgets.QFrame(self.page)
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout.addWidget(self.frame_1)
        self.stackedWidget.addWidget(self.page)
        self.browser = QWebEngineView(self.stackedWidget)
        self.browser.load(
            QUrl("file:///E:/code/python/inflight_project/client.html"))
        hboxlayout = QHBoxLayout(self.frame_1)
        hboxlayout.addWidget(self.browser)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(0, 20, 201, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 70, 201, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 120, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 170, 201, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 220, 201, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 270, 201, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionshujuqingxi = QtWidgets.QAction(MainWindow)
        self.actionshujuqingxi.setObjectName("actionshujuqingxi")
        self.actionshujuguiyue = QtWidgets.QAction(MainWindow)
        self.actionshujuguiyue.setObjectName("actionshujuguiyue")
        self.actionshujubianhuan = QtWidgets.QAction(MainWindow)
        self.actionshujubianhuan.setObjectName("actionshujubianhuan")
        self.actionshujupingfen = QtWidgets.QAction(MainWindow)
        self.actionshujupingfen.setObjectName("actionshujupingfen")
        self.menu_2.addAction(self.actionshujuqingxi)
        self.menu_2.addAction(self.actionshujuguiyue)
        self.menu_2.addAction(self.actionshujubianhuan)
        self.menu_2.addAction(self.actionshujupingfen)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "总里程"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "最近飞行时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "总消费金额"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "客户类型"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "列表"))
        self.pushButton_7.setText(_translate("MainWindow", "饼状图"))
        self.pushButton_8.setText(_translate("MainWindow", "折线图"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "图表"))
        self.pushButton.setText(_translate("MainWindow", "全部客户"))
        self.pushButton_2.setText(_translate("MainWindow", "重要保持客户"))
        self.pushButton_3.setText(_translate("MainWindow", "重要发展客户"))
        self.pushButton_4.setText(_translate("MainWindow", "重要挽留客户"))
        self.pushButton_5.setText(_translate("MainWindow", "一般客户"))
        self.pushButton_6.setText(_translate("MainWindow", "低价值客户"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "客户价值"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "数据预测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "决策推荐"))
        self.menu.setTitle(_translate("MainWindow", "打开文件"))
        self.menu_2.setTitle(_translate("MainWindow", "处理文件"))
        self.menu_3.setTitle(_translate("MainWindow", "可视化管理"))
        self.menu_4.setTitle(_translate("MainWindow", "设置"))
        self.menu_5.setTitle(_translate("MainWindow", "帮助"))
        self.menu_6.setTitle(_translate("MainWindow", "关于"))
        self.actionshujuqingxi.setText(_translate("MainWindow", "数据清洗"))
        self.actionshujuguiyue.setText(_translate("MainWindow", "数据规约"))
        self.actionshujubianhuan.setText(_translate("MainWindow", "数据变换"))
        self.actionshujupingfen.setText(_translate("MainWindow", "数据评分"))

