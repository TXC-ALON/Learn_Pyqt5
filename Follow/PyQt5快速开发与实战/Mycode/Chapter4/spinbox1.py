import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建QSpinBox控件和QLabel控件
        self.spinBox = QSpinBox()
        self.label = QLabel()

        # 设置初始值和范围
        self.spinBox.setValue(0)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)

        # 创建垂直布局，将控件添加到布局中
        vbox = QVBoxLayout()
        vbox.addWidget(self.spinBox)
        vbox.addWidget(self.label)

        # 设置主布局
        self.setLayout(vbox)

        # 连接信号槽，当值发生变化时更新QLabel控件
        self.spinBox.valueChanged.connect(self.updateLabel)

        # 设置窗口标题和大小
        self.setWindowTitle('SpinBox Demo')
        self.setGeometry(300, 300, 250, 150)
        self.label.setText('Current Value: {}'.format(self.spinBox.value()))

    def updateLabel(self):
        # 当QSpinBox的值发生变化时，更新QLabel的文本内容
        self.label.setText('Current Value: {}'.format(self.spinBox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
