import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPen, QPainter, QPainterPath, QBrush
from PyQt5.QtCore import QPointF, Qt, QTimer


class Taichi(QWidget):
    def __init__(self, speed = 5,parent=None):
        super().__init__(parent)
        self.resize(600, 500)
        self.angle = 0  # Initial angle is 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotateTaiChi)
        self.timer.start(speed)  # Set the timer interval in milliseconds

    def rotateTaiChi(self):
        self.angle -= 5  # Update the angle
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center = QPointF(self.width() / 2, self.height() / 2)
        r = min(self.width(), self.height()) / 3  # Outer circle radius
        r1 = r / 7  # Inner circle radius

        path = QPainterPath()  # Create a QPainterPath to draw the Tai Chi symbol
        path.moveTo(center.x(), center.y() - r)
        path.arcTo(center.x() - r, center.y() - r, 2 * r, 2 * r, 90, 360)  # Outer circle
        path.arcTo(center.x() - r, center.y() - r, 2 * r, 2 * r, 90, -180)  # Inverted semicircle

        path.moveTo(center.x(), center.y() + r)
        path.arcTo(center.x() - r / 2, center.y(), r, r, -90, 180)  # Upper semicircle
        path.arcTo(center.x() - r / 2, center.y() - r / 2 - r / 2, r, r, 270, -180)  # Lower semicircle

        path.moveTo(center.x() + r1, center.y() - r / 2)
        path.arcTo(center.x() - r1, center.y() - r / 2 - r1, 2 * r1, 2 * r1, 0, 360)  # Upper inner circle
        path.moveTo(center.x() + r1, center.y() + r / 2)
        path.arcTo(center.x() - r1, center.y() + r / 2 - r1, 2 * r1, 2 * r1, 0, -360)  # Lower inner circle -360决定是外部，所以是白色。

        path.setFillRule(Qt.WindingFill)  # Set the filling rule
        # Qt.WindingFill：该填充规则使用非零环绕数算法，根据路径的方向来决定哪些区域被认为是内部区域，哪些是外部区域。对于每个顺时针方向的闭合路径，环绕数会递增；对于每个逆时针方向的闭合路径，环绕数会递减。最终，根据环绕数的正负来确定填充区域。
        # Qt.OddEvenFill：该填充规则使用奇偶规则，不考虑路径的方向。填充区域被路径交叉的次数决定，如果交叉次数是奇数，则被认为是内部区域；如果交叉次数是偶数，则被认为是外部区域。
        # # Rotate the painter around the center point and draw the Tai Chi symbol
        painter.translate(center.x(), center.y())
        painter.rotate(self.angle)
        painter.translate(-center.x(), -center.y())

        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.black)
        painter.setPen(pen)

        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawPath(path)

        super().paintEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()
    sys.exit(app.exec())
