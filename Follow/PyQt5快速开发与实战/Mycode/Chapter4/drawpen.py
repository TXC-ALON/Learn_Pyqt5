import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Drawing(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('钢笔样式例子')

        # 创建水平布局管理器
        hlayout = QHBoxLayout(self)

        # 创建 QFrame 组件并设置样式
        frame = QFrame(self)
        frame.setStyleSheet("background-color: white;")

        # 将 QFrame 添加到水平布局管理器中
        hlayout.addWidget(frame)

        # 创建垂直布局管理器
        vlayout = QVBoxLayout(frame)

        # 创建画布组件
        self.canvas = Canvas(self)

        # 将画布组件添加到垂直布局管理器中，并设置拉伸因子为 1
        vlayout.addWidget(self.canvas, 1)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.canvas.update()

class Canvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        height = self.height()  # 获取窗口的高度
        interval = height // 7  # 计算线条之间的间距

        y = int(interval/2)  # 初始化 y 坐标为第一个线条的起点
        for i in range(6):
            qp.setPen(pen)
            qp.drawLine(20, y, self.width()-20, y)

            y += interval  # 更新 y 坐标为下一个线条的起点

            pen.setStyle(pen.style() + 1)  # 切换线条样式

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, y, self.width()-20, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Drawing()
    demo.resize(280, 270)
    demo.show()
    sys.exit(app.exec_())
