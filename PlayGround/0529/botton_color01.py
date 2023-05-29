import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, PrimaryPushButton,
                            HyperlinkButton, setTheme, Theme, ToolButton, ToggleButton, RoundMenu,
                            SplitPushButton, SplitToolButton, PrimaryToolButton, PrimarySplitPushButton,
                            PrimarySplitToolButton, PrimaryDropDownPushButton, PrimaryDropDownToolButton)
from qfluentwidgets import FluentIcon as FIF


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.clicknum = 0
        self.initUI()

    def initUI(self):

        # Create the button
        self.btn = PushButton('Button', self)
        self.btn.setCheckable(True)

        # Set the size and position of the button
        self.btn.setGeometry(10, 10, 150, 50)

        # Set the initial background color to red
        self.btn.setStyleSheet('QPushButton {background-color: yellow;border-radius: 5px;}')

        # Connect signals to slots

        self.btn.clicked.connect(self.changeColor)
        self.btn.released.connect(self.revertColor)
        self.btn.pressed.connect(self.setPressedColor)

        # 连接 enterEvent 和 leaveEvent 信号
        self.btn.enterEvent = self.enterMethod
        self.btn.leaveEvent = self.leaveMethod

    def enterMethod(self, event):
        # 鼠标进入按钮区域时，更改按钮的样式和提示信息
        self.btn.setToolTip('Mouse is hover over me')
        self.btn.setStyleSheet(
            "PushButton {background-color:green; color:white;border-radius: 5px;} QToolTip {color:red;}")
        #self.btn.setStyleSheet('background-color:green;color:white')

    def leaveMethod(self, event):
        # 鼠标离开按钮区域时，还原按钮的样式和提示信息
        self.btn.setStyleSheet('')
        QToolTip.hideText()

    def changeColor(self):
        if (self.clicknum % 2 == 0):
            self.btn.setStyleSheet('PushButton {background-color: blue;border-radius: 5px;}')
        else:
            self.btn.setStyleSheet('PushButton {border-radius: 5px;}')
        self.clicknum += 1
        print(self.clicknum)

    def revertColor(self):
        self.btn.setStyleSheet('PushButton {background-color: red;border-radius: 5px;}')

    def setPressedColor(self):
        self.btn.setStyleSheet('PushButton {background-color: green;border-radius: 5px;}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
