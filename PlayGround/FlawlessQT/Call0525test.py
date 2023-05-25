from PyQt5.QtWidgets import QApplication, QMainWindow
from navigation import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 使用转换的UI文件中的类来设置UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication([])

    # 创建主窗口
    window = MainWindow()

    # 显示主窗口
    window.show()

    # 启动应用程序的事件循环
    app.exec_()
