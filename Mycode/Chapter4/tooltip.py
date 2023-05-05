from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个按钮
        self.button = QPushButton("Click me", self)
        self.button.setGeometry(50, 50, 100, 50)

        # 设置气泡提示文本
        self.button.setToolTip("Hello, world!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
