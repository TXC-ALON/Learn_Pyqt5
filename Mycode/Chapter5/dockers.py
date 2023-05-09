from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QWidget, QPushButton, QVBoxLayout


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建两个可停靠窗口并添加文本编辑控件
        dock1 = QDockWidget("Dock 1", self)
        text_edit1 = QTextEdit()
        text_edit1.setPlainText("This is Dock 1")
        dock1.setWidget(text_edit1)

        dock2 = QDockWidget("Dock 2", self)
        text_edit2 = QTextEdit()
        text_edit2.setPlainText("This is Dock 2")
        dock2.setWidget(text_edit2)

        dock3 = QDockWidget("Dock 3", self)
        text_edit3 = QTextEdit()
        text_edit3.setPlainText("This is Dock 3")
        dock3.setWidget(text_edit3)

        dock4 = QDockWidget("Dock 4", self)
        text_edit4 = QTextEdit()
        text_edit4.setPlainText("This is Dock 4")
        dock4.setWidget(text_edit4)

        # 创建一个按钮
        button = QPushButton("Click Me")

        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 设置主窗口属性
        self.setWindowTitle("My Window")
        # 添加可停靠窗口到主窗口
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)
        self.addDockWidget(Qt.TopDockWidgetArea, dock3)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock4)

        # 设置主窗口属性
        self.setWindowTitle("My Window")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
