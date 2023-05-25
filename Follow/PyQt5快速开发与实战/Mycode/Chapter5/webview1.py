import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        print(1)
        self.setWindowTitle("百度主页")
        print(2)
        self.setGeometry(100, 100, 800, 600)
        print(3)

        self.browser = QWebEngineView()
        print(4)
        self.browser.load(QUrl('https://www.baidu.com'))
        print(5)
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
