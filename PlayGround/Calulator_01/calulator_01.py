# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calulator_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TextEdit = TextEdit(self.frame)
        self.TextEdit.setObjectName("TextEdit")
        self.gridLayout_3.addWidget(self.TextEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PushButton = PushButton(self.groupBox_2)
        self.PushButton.setObjectName("PushButton")
        self.gridLayout_2.addWidget(self.PushButton, 0, 0, 1, 1)
        self.PushButton_2 = PushButton(self.groupBox_2)
        self.PushButton_2.setObjectName("PushButton_2")
        self.gridLayout_2.addWidget(self.PushButton_2, 0, 1, 1, 1)
        self.PushButton_3 = PushButton(self.groupBox_2)
        self.PushButton_3.setObjectName("PushButton_3")
        self.gridLayout_2.addWidget(self.PushButton_3, 0, 2, 1, 1)
        self.PushButton_4 = PushButton(self.groupBox_2)
        self.PushButton_4.setObjectName("PushButton_4")
        self.gridLayout_2.addWidget(self.PushButton_4, 0, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 1, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 2, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 2, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 2, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 2, 3, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 3, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 3, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 3, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_2.addWidget(self.pushButton_24, 3, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 4, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 4, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 4, 2, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 4, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 5, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Calulator"))
        self.groupBox_2.setTitle(_translate("MainWindow", "BaseDiag"))
        self.PushButton.setText(_translate("MainWindow", "x^2"))
        self.PushButton_2.setText(_translate("MainWindow", "1/x"))
        self.PushButton_3.setText(_translate("MainWindow", "|x|"))
        self.PushButton_4.setText(_translate("MainWindow", "n!"))
        self.pushButton_9.setText(_translate("MainWindow", "("))
        self.pushButton_11.setText(_translate("MainWindow", ")"))
        self.pushButton_10.setText(_translate("MainWindow", "CE"))
        self.pushButton_12.setText(_translate("MainWindow", "/"))
        self.pushButton_13.setText(_translate("MainWindow", "7"))
        self.pushButton_15.setText(_translate("MainWindow", "8"))
        self.pushButton_14.setText(_translate("MainWindow", "9"))
        self.pushButton_16.setText(_translate("MainWindow", "*"))
        self.pushButton_23.setText(_translate("MainWindow", "4"))
        self.pushButton_22.setText(_translate("MainWindow", "5"))
        self.pushButton_21.setText(_translate("MainWindow", "6"))
        self.pushButton_24.setText(_translate("MainWindow", "-"))
        self.pushButton_17.setText(_translate("MainWindow", "1"))
        self.pushButton_19.setText(_translate("MainWindow", "2"))
        self.pushButton_18.setText(_translate("MainWindow", "3"))
        self.pushButton_20.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "+/-"))
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "."))
        self.pushButton_4.setText(_translate("MainWindow", "="))
from qfluentwidgets import PushButton, TextEdit
