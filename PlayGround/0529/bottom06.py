from PyQt5.QtGui import QFontMetrics, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt


class MyBotton(QPushButton):
    def __init__(self, _text, _col, _row):
        super().__init__(_text)
        self.col = _col
        self.row = _row
        self.clicknum = 0
        pal = self.palette()
        pal.setColor(QPalette.Button, QColor(Qt.red))
        self.setAutoFillBackground(True)
        self.setPalette(pal)


class TestBotton(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('Calculator{background:white}')
        self.setWindowTitle("TestBotton")
        self.setMinimumHeight(560)  # 设置窗口的最小高度为500像素
        self.setMinimumWidth(300)  # 设置窗口的最小宽度为300像素
        self.resize(400, 600)  # 设置默认宽度和高度

        buttons = [
            '%', 'CE', 'C', 'Del',
            '1/x', 'x^2', '√(x)', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '=',
        ]

        self.btn = MyBotton(buttons[0], 0, 0)
        self.btn.setCheckable(True)
        self.btn.setStyleSheet('QPushButton {height:50px;background-color: yellow;border-radius: 5px;}')
        self.btn.clicked.connect(self.changeColor)

        # 创建一个 QVBoxLayout 布局管理器
        vbox = QVBoxLayout()
        # 将按钮添加到布局管理器中
        vbox.addWidget(self.btn)

        # 设置布局管理器
        self.setLayout(vbox)


    def changeColor(self):
            self.btn.setStyleSheet('QPushButton {height:100px;border-radius: 5px;}')



if __name__ == '__main__':
    app = QApplication([])
    TestBotton = TestBotton()
    TestBotton.show()
    app.exec()
