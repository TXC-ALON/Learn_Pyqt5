from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 QPushButton 对象
        self.btn = QPushButton('Button', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)

        # 连接 enterEvent 和 leaveEvent 信号
        self.btn.enterEvent = self.enterMethod
        self.btn.leaveEvent = self.leaveMethod

    def enterMethod(self, event):
        # 鼠标进入按钮区域时，更改按钮的样式和提示信息
        self.btn.setStyleSheet('background-color:green;color:white')
        QToolTip.setFont(QApplication.font())
        QToolTip.showText(event.globalPos() + self.btn.rect().bottomRight(),
                          'Mouse is hovering over me', self.btn,
                          QRect(0, 0, 100, 30))  # 设置 tooltip 的大小和样式

    def leaveMethod(self, event):
        # 鼠标离开按钮区域时，还原按钮的样式和提示信息
        self.btn.setStyleSheet('')
        QToolTip.hideText()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()
