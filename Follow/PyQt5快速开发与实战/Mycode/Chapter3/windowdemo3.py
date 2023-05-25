from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个中心小部件并设置布局管理器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建垂直布局管理器和两个水平布局管理器
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        # 将两个水平布局管理器添加到垂直布局管理器中
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        # 创建两个按钮并将其添加到第一个水平布局管理器中
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        hbox1.addWidget(button1)
        hbox1.addWidget(button2)

        # 创建一个按钮并将其添加到第二个水平布局管理器中
        button3 = QPushButton('Button 3')
        hbox2.addWidget(button3)

        # 设置窗口的布局管理器
        central_widget.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
