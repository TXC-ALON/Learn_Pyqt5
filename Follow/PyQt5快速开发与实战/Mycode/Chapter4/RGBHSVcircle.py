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
        self.hue_slider = QSlider(Qt.Horizontal)
        self.saturation_slider = QSlider(Qt.Horizontal)
        self.value_slider = QSlider(Qt.Horizontal)

        self.red_slider.setMinimum(0)
        self.red_slider.setMaximum(255)
        self.green_slider.setMinimum(0)
        self.green_slider.setMaximum(255)
        self.blue_slider.setMinimum(0)
        self.blue_slider.setMaximum(255)
        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(180)
        self.saturation_slider.setMinimum(0)
        self.saturation_slider.setMaximum(255)
        self.value_slider.setMinimum(0)
        self.value_slider.setMaximum(255)

        self.red_slider.valueChanged.connect(self.update_from_rgb)
        self.green_slider.valueChanged.connect(self.update_from_rgb)
        self.blue_slider.valueChanged.connect(self.update_from_rgb)
        self.hue_slider.valueChanged.connect(self.update_from_hsv)
        self.saturation_slider.valueChanged.connect(self.update_from_hsv)
        self.value_slider.valueChanged.connect(self.update_from_hsv)

        self.red_value_label = QLabel("0")
        self.green_value_label = QLabel("0")
        self.blue_value_label = QLabel("0")
        self.hue_value_label = QLabel("0")
        self.saturation_value_label = QLabel("0")
        self.value_value_label = QLabel("0")

        rgb_layout = QHBoxLayout()
        rgb_layout.addWidget(QLabel("R"))
        rgb_layout.addWidget(self.red_slider)
        rgb_layout.addWidget(self.red_value_label)
        rgb_layout.addWidget(QLabel("G"))
        rgb_layout.addWidget(self.green_slider)
        rgb_layout.addWidget(self.green_value_label)
        rgb_layout.addWidget(QLabel("B"))
        rgb_layout.addWidget(self.blue_slider)
        rgb_layout.addWidget(self.blue_value_label)

        hsv_layout = QHBoxLayout()
        hsv_layout.addWidget(QLabel("H"))
        hsv_layout.addWidget(self.hue_slider)
        hsv_layout.addWidget(self.hue_value_label)
        hsv_layout.addWidget(QLabel("S"))
        hsv_layout.addWidget(self.saturation_slider)
        hsv_layout.addWidget(self.saturation_value_label)
        hsv_layout.addWidget(QLabel("V"))
        hsv_layout.addWidget(self.value_slider)
        hsv_layout.addWidget(self.value_value_label)

        layout = QVBoxLayout()
        layout.addWidget(self.circle_widget)
        layout.addLayout(rgb_layout)
        layout.addLayout(hsv_layout)


        self.setLayout(layout)

    def update_from_rgb(self):
        r = self.red_slider.value()
        g = self.green_slider.value()
        b = self.blue_slider.value()

        self.red_value_label.setText(str(r))
        self.green_value_label.setText(str(g))
        self.blue_value_label.setText(str(b))

        color = QColor(r, g, b)
        h, s, v, _ = color.getHsv()

        self.hue_slider.blockSignals(True)
        self.saturation_slider.blockSignals(True)
        self.value_slider.blockSignals(True)

        self.hue_slider.setValue(h)
        self.saturation_slider.setValue(s)
        self.value_slider.setValue(v)

        self.hue_value_label.setText(str(h))
        self.saturation_value_label.setText(str(s))
        self.value_value_label.setText(str(v))

        self.hue_slider.blockSignals(False)
        self.saturation_slider.blockSignals(False)
        self.value_slider.blockSignals(False)

        self.circle_widget.setRed(r)
        self.circle_widget.setGreen(g)
        self.circle_widget.setBlue(b)

    def update_from_hsv(self):
        h = self.hue_slider.value()
        s = self.saturation_slider.value()
        v = self.value_slider.value()

        self.hue_value_label.setText(str(h))
        self.saturation_value_label.setText(str(s))
        self.value_value_label.setText(str(v))

        color = QColor.fromHsv(h, s, v)
        r, g, b, _ = color.getRgb()

        self.red_slider.blockSignals(True)
        self.green_slider.blockSignals(True)
        self.blue_slider.blockSignals(True)

        self.red_slider.setValue(r)
        self.green_slider.setValue(g)
        self.blue_slider.setValue(b)

        self.red_value_label.setText(str(r))
        self.green_value_label.setText(str(g))
        self.blue_value_label.setText(str(b))

        self.red_slider.blockSignals(False)
        self.green_slider.blockSignals(False)
        self.blue_slider.blockSignals(False)

        self.circle_widget.setRed(r)
        self.circle_widget.setGreen(g)
        self.circle_widget.setBlue(b)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
