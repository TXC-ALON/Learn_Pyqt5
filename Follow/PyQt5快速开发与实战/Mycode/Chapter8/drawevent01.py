import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制矩形")
        self.rectangles = []
        self.current_rectangle = None
        self.dragging = False
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.current_rectangle = QRect(event.pos(), event.pos())
            self.dragging = True
            self.update()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.current_rectangle.setBottomRight(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.dragging:
            self.dragging = False
            self.rectangles.append(self.current_rectangle)
            self.current_rectangle = None
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor(0, 0, 0), 2))

        for rectangle in self.rectangles:
            painter.drawRect(rectangle)

        if self.dragging and self.current_rectangle is not None:
            painter.setPen(QPen(QColor(0, 0, 0), 2, Qt.DashLine))
            painter.drawRect(self.current_rectangle)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
