# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P3DS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import EditableComboBox, PrimaryPushButton, PushButton, TextEdit

class Ui_P3DS_Launcher(object):
    def setupUi(self, P3DS_Launcher):
        P3DS_Launcher.setObjectName("P3DS_Launcher")
        P3DS_Launcher.resize(1500, 550)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(P3DS_Launcher)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GB_Compile = QtWidgets.QGroupBox(P3DS_Launcher)
        self.GB_Compile.setTitle("")
        self.GB_Compile.setObjectName("GB_Compile")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GB_Compile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GB_Launch = QtWidgets.QGroupBox(self.GB_Compile)
        self.GB_Launch.setObjectName("GB_Launch")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.GB_Launch)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ECB_Choice = EditableComboBox(self.GB_Launch)
        self.ECB_Choice.setObjectName("ECB_Choice")
        self.ECB_Choice.setFont(font)
        self.ECB_Choice.setMinimumWidth(250)
        self.ECB_Choice.addItem("Version 1208")
        self.ECB_Choice.addItem("Version 1209")
        self.ECB_Choice.addItem("Version 1210")
        self.ECB_Choice.setFixedHeight(50)
        self.horizontalLayout_3.addWidget(self.ECB_Choice)
        self.PB_Launch = PrimaryPushButton(self.GB_Launch)
        self.PB_Launch.setFixedWidth(150)
        self.PB_Launch.setFont(font)
        self.PB_Launch.setObjectName("PB_Launch")
        self.horizontalLayout_3.addWidget(self.PB_Launch)
        self.verticalLayout.addWidget(self.GB_Launch)
        self.PB_Clear_Output = PushButton(self.GB_Compile)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PB_Clear_Output.setFont(font)
        self.PB_Clear_Output.setObjectName("PB_Clear_Output")
        self.verticalLayout.addWidget(self.PB_Clear_Output)
        self.GB_Check = QtWidgets.QGroupBox(self.GB_Compile)
        self.GB_Check.setObjectName("GB_Check")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.GB_Check)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CB_Compile_OC = QtWidgets.QCheckBox(self.GB_Check)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        #font.setKerning(True)
        self.CB_Compile_OC.setFont(font)
        self.CB_Compile_OC.setObjectName("CB_Compile_OC")
        self.CB_Compile_OC.setChecked(True)
        self.horizontalLayout.addWidget(self.CB_Compile_OC)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CB_Move = QtWidgets.QCheckBox(self.GB_Check)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.CB_Move.setFont(font)
        self.CB_Move.setObjectName("CB_Move")
        self.CB_Move.setChecked(True)
        self.horizontalLayout.addWidget(self.CB_Move)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CB_Launch = QtWidgets.QCheckBox(self.GB_Check)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CB_Launch.setFont(font)
        self.CB_Launch.setObjectName("CB_Launch")
        self.horizontalLayout.addWidget(self.CB_Launch)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.GB_Check)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.PB_Process = PrimaryPushButton(self.GB_Compile)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.PB_Process.setFont(font)
        self.PB_Process.setObjectName("PB_Process")
        self.verticalLayout.addWidget(self.PB_Process)
        self.PB_Compile_All = PushButton(self.GB_Compile)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PB_Compile_All.setFont(font)
        self.PB_Compile_All.setAutoFillBackground(False)
        self.PB_Compile_All.setObjectName("PB_Compile_All")
        self.verticalLayout.addWidget(self.PB_Compile_All)
        self.horizontalLayout_2.addWidget(self.GB_Compile)
        self.Output = TextEdit(P3DS_Launcher)
        self.Output.setObjectName("Output")
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Output.setFont(font)
        self.horizontalLayout_2.addWidget(self.Output)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(P3DS_Launcher)
        self.PB_Launch.clicked.connect(self.launch)
        self.PB_Clear_Output.clicked.connect(self.Output.clear)  # type: ignore
        self.PB_Process.clicked.connect(self.process)  # type: ignore
        self.PB_Compile_All.clicked.connect(self.compile_all)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(P3DS_Launcher)

    def retranslateUi(self, P3DS_Launcher):
        _translate = QtCore.QCoreApplication.translate
        P3DS_Launcher.setWindowTitle(_translate("P3DS_Launcher", "P3DS_Launcher"))
        self.GB_Launch.setTitle(_translate("P3DS_Launcher", "启动项"))
        self.PB_Launch.setText(_translate("P3DS_Launcher", "启动"))
        self.PB_Clear_Output.setText(_translate("P3DS_Launcher", "清空输出"))
        self.GB_Check.setTitle(_translate("P3DS_Launcher", "编译"))
        self.CB_Compile_OC.setText(_translate("P3DS_Launcher", "编译(仅C++)"))
        self.CB_Move.setText(_translate("P3DS_Launcher", "移动"))
        self.CB_Launch.setText(_translate("P3DS_Launcher", "启动"))
        self.PB_Process.setText(_translate("P3DS_Launcher", "执行"))
        self.PB_Compile_All.setText(_translate("P3DS_Launcher", "全部重新编译"))

    def launch(self):
        version = self.ECB_Choice.currentText()
        str = "Launch! "+version
        self.Output.append(str)

    def process(self):
        self.Output.append("Process")

    def compile_all(self):
        self.Output.append("CompileAll")