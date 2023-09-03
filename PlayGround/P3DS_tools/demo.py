import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QAction, QGridLayout, QMainWindow
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, PrimaryPushButton,
                            HyperlinkButton, setTheme, Theme, ToolButton, ToggleButton, RoundMenu,
                            SplitPushButton, SplitToolButton, PrimaryToolButton, PrimarySplitPushButton,
                            PrimarySplitToolButton, PrimaryDropDownPushButton, PrimaryDropDownToolButton)
from qfluentwidgets import FluentIcon as FIF
from view.UI_P3DS import Ui_P3DS_Launcher

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 使用转换的UI文件中的类来设置UI
        self.ui = Ui_P3DS_Launcher()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())