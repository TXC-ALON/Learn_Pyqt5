import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QSizeGrip


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('自动调整大小的示例程序')

        # 创建一个标签和文本框以接收用户输入
        input_label = QLabel('输入：', self)
        input_textbox = QLineEdit(self)
        input_textbox.textChanged.connect(self.updateOutput)

        # 创建一个标签来显示输出值
        output_label = QLabel('输出：', self)
        self.output_value = QLabel('', self)
        self.output_value.setMinimumWidth(50)

        # 创建一个垂直布局，并将所有小部件添加到其中
        layout = QVBoxLayout()
        layout.addWidget(input_label)
        layout.addWidget(input_textbox)
        layout.addWidget(output_label)
        layout.addWidget(self.output_value)

        # 创建一个QWidget并将垂直布局设置为其布局
        widget = QWidget()
        widget.setLayout(layout)

        # 将QWidget设置为主窗口的中心小部件
        self.setCentralWidget(widget)

        # 添加QSizeGrip小部件
        self.sizegrip = QSizeGrip(self)
        self.statusBar().addPermanentWidget(self.sizegrip)

    def resizeEvent(self, event):
        # 在窗口大小更改时重新定位QSizeGrip小部件
        self.statusBar().move(self.width() - self.statusBar().width(), self.height() - self.statusBar().height())

    def updateOutput(self, text):
        # 根据用户输入计算输出值
        try:
            output = str(float(text) ** 2)
        except ValueError:
            output = ''
        self.output_value.setText(output)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
