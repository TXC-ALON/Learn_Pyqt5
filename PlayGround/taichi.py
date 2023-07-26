import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer, QPoint


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 500)
        self.angle = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        w, h = self.width(), self.height()
        center = QPoint(w / 2, h / 2)
        radius = min(w, h) / 3
        painter.translate(center)  # 将坐标原点移动到中心

        # 绘制太极图
        path = QPainterPath()
        path.addEllipse(-radius, -radius, 2 * radius, 2 * radius)  # 外圆
        path.arcMoveTo(-radius, -radius/2, radius*2, radius, 90)  # 下半部分圆弧起点
        path.arcTo(-radius, -radius/2, radius*2, radius, 90, -180)  # 下半部分圆弧
        path.arcMoveTo(-radius, 0, radius*2, radius, 270)  # 上半部分圆弧起点
        path.arcTo(-radius, 0, radius*2, radius, 270, -180)  # 上半部分圆弧
        painter.setPen(QPen(Qt.NoPen))

        # 绘制阴阳鱼
        brush = QBrush(Qt.SolidPattern)
        painter.save()

        # 绘制黑色部分
        painter.setBrush(Qt.black)
        rotate_angle = self.angle % 360
        painter.drawPie(-radius, -radius, 2 * radius, 2 * radius, 90 * 16, -180 * 16)
        painter.drawChord(-radius, -radius, 2 * radius, 2 * radius, 90 * 16, -180 * 16)

        # 绘制白色部分
        painter.setBrush(Qt.white)
        painter.drawPie(-radius, -radius, 2 * radius, 2 * radius, rotate_angle * 16, -180 * 16)
        painter.drawChord(-radius, -radius, 2 * radius, 2 * radius, rotate_angle * 16, -180 * 16)

        painter.restore()

    def closeEvent(self, event):
        self.timer.stop()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
