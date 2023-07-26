import sys
import time
import psutil

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget, QFrame, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap
# import res


class NetWindows(QMainWindow):
    net_signal = pyqtSignal(str, str)

    def __init__(self):
        super(NetWindows, self).__init__()
        self.ui_init()
        self.thread_init()

    def ui_init(self):
        self.setWindowTitle('网速')
        self.resize(200, 80)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 窗口始终显示在最前面
        self.upload_icon = QLabel()
        self.upload_icon.setPixmap(QPixmap(':res/upload.png'))
        self.upload_icon.setScaledContents(True)
        self.download_icon = QLabel()
        self.download_icon.setPixmap(QPixmap(':res/download.png'))
        self.download_icon.setScaledContents(True)
        self.upload_text = QLabel()
        self.upload_text.setText('upload: ')
        self.download_text = QLabel()
        self.download_text.setText('download: ')

        self.upload_lab = QLabel()
        self.download_lab = QLabel()

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.upload_icon, 0, 0, 1, 1)
        self.g_layout.addWidget(self.download_icon, 1, 0, 1, 1)
        self.g_layout.addWidget(self.upload_text, 0, 1, 1, 1)
        self.g_layout.addWidget(self.download_text, 1, 1, 1, 1)
        self.g_layout.addWidget(self.upload_lab, 0, 2, 1, 4)
        self.g_layout.addWidget(self.download_lab, 1, 2, 1, 4)
        self.widget = QWidget()
        self.widget.setLayout(self.g_layout)
        self.setCentralWidget(self.widget)

    def thread_init(self):
        self.net_thread = NetThread()
        self.net_thread.net_signal.connect(self.net_slot)
        self.net_thread.start(1000)

    def variate_init(self):
        self.upload_content = ''
        self.download_content = ''

    def net_slot(self, upload_content, download_content):
        self.upload_lab.setText(upload_content)
        self.download_lab.setText(download_content)

    def mousePressEvent(self, event):
        '''
        重写按下事件
        '''
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseMoveEvent(self, event):
        '''
        重写移动事件
        '''
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)


class NetThread(QThread):
    net_signal = pyqtSignal(str, str)

    def __init__(self):
        super(NetThread, self).__init__()

    def net_func(self):
        parameter = psutil.net_io_counters()
        recv1 = parameter[1]  # 接收数据
        send1 = parameter[0]  # 上传数据
        time.sleep(1)  # 每隔1s监听端口接收数据
        parameter = psutil.net_io_counters()
        recv2 = parameter[1]
        send2 = parameter[0]
        self.upload_content = '{:.1f} kb/s.'.format((send2 - send1) / 1024.0)
        self.download_content = '{:.1f} kb/s.'.format((recv2 - recv1) / 1024.0)

    def run(self):
        while (1):
            self.net_func()
            self.net_signal.emit(self.upload_content, self.download_content)
            time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dispaly = NetWindows()
    dispaly.show()
    netwidows = NetWindows()
    sys.exit(app.exec_())

