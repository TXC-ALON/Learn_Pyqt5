from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个中心小部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 在中心小部件中创建一个垂直布局
        layout = QVBoxLayout(central_widget)

        # 创建一个标签和文本框
        self.label = QLabel('请输入文本:', self)
        self.textbox = QLineEdit(self)
        self.textbox.returnPressed.connect(self.on_return_pressed)

        # 将标签和文本框添加到布局中
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)

    def on_return_pressed(self):
        # 从文本框中获取输入文本
        text = self.textbox.text()

        # 创建一个标签以显示输出
        output_label = QLabel(f"你输入了: {text}", self)
        output_label.setAlignment(Qt.AlignCenter)

        # 在布局中添加输出标签
        self.layout().addWidget(output_label)

        # 调整窗口大小以适应内容
        self.adjustSize()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
