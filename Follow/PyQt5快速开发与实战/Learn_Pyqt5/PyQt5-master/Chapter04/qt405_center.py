# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5将窗口放在屏幕中间例子
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys


class Winform(QMainWindow):

    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)

        self.setWindowTitle('主窗口放在屏幕中间例子')
        self.resize(800, 600)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x = int((screen.width() - size.width()) / 2)
        y = int((screen.height() - size.height()) / 2)
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
