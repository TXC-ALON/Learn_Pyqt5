import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush


class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.red = 0
        self.green = 0
        self.blue = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(QColor(self.red, self.green, self.blue)))
        painter.drawEllipse(self.rect().center(), 50, 50)

    def setRed(self, value):
        self.red = value
        self.update()

    def setGreen(self, value):
        self.green = value
        self.update()

    def setBlue(self, value):
        self.blue = value
        self.update()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.circle_widget = CircleWidget(self)

        self.red_slider = QSlider(Qt.Horizontal)
        self.green_slider = QSlider(Qt.Horizontal)
        self.blue_slider = QSlider(Qt.Horizontal)

        self.red_slider.setMaximum(255)
        self.green_slider.setMaximum(255)
        self.blue_slider.setMaximum(255)

        self.red_slider.valueChanged.connect(self.circle_widget.setRed)
        self.green_slider.valueChanged.connect(self.circle_widget.setGreen)
        self.blue_slider.valueChanged.connect(self.circle_widget.setBlue)

        self.red_value_label = QLabel("0")
        self.green_value_label = QLabel("0")
        self.blue_value_label = QLabel("0")

        self.red_slider.valueChanged.connect(lambda value: self.red_value_label.setText(str(value)))
        self.green_slider.valueChanged.connect(lambda value: self.green_value_label.setText(str(value)))
        self.blue_slider.valueChanged.connect(lambda value: self.blue_value_label.setText(str(value)))

        sliders_layout = QHBoxLayout()
        sliders_layout.addWidget(QLabel("R"))
        sliders_layout.addWidget(self.red_slider)
        sliders_layout.addWidget(self.red_value_label)
        sliders_layout.addWidget(QLabel("G"))
        sliders_layout.addWidget(self.green_slider)
        sliders_layout.addWidget(self.green_value_label)
        sliders_layout.addWidget(QLabel("B"))
        sliders_layout.addWidget(self.blue_slider)
        sliders_layout.addWidget(self.blue_value_label)

        layout = QVBoxLayout()
        layout.addWidget(self.circle_widget)
        layout.addLayout(sliders_layout)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
