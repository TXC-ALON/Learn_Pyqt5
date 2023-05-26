from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt
import math
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, PrimaryPushButton,
                            HyperlinkButton, setTheme, Theme, ToolButton, ToggleButton, RoundMenu,
                            SplitPushButton, SplitToolButton, PrimaryToolButton, PrimarySplitPushButton,
                            PrimarySplitToolButton, PrimaryDropDownPushButton, PrimaryDropDownToolButton)
from qfluentwidgets import FluentIcon as FIF


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setMinimumHeight(560)  # 设置窗口的最小高度为500像素
        # 创建一个 QLineEdit 用于显示计算结果
        self.result_display = QLineEdit('0')
        # self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 设置文本从右往左增长并垂直居中

        # 创建按键，并为数字、运算符、括号和等号分组 6*4
        buttons = [
            '%', 'CE', 'C', 'Del',
            '1/x', 'x^2', '√(x)', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '=',
        ]

        # 创建按钮网格布局
        grid_layout = QGridLayout()
        grid_layout.setSpacing(5)  # 设置按钮之间的间距

        # 将按键添加到网格布局
        row, col = 0, 0
        for button in buttons:
            button_obj = PushButton(button)
            grid_layout.addWidget(button_obj, row, col)
            button_obj.clicked.connect(self.handle_button_click)
            button_obj.setStyleSheet("QPushButton { font-size: 20px; text-align: center; }")  # 设置按钮文本的字体大小和居中对齐
            button_obj.setStyleSheet("background-color: rgb(200, 200, 255);")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # 设置主布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_display)
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

        # 设置控件的大小策略
        self.result_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置QLineEdit水平方向自动拉伸，垂直方向固定大小
        self.result_display.setMinimumHeight(30)  # 设置最小高度为30px
        self.result_display.setMaximumHeight(100)  # 设置最小高度为30px
        for i in range(grid_layout.count()):
            widget = grid_layout.itemAt(i).widget()
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置按钮自动拉伸

    def setButtonStyle(self):
        # 获取按钮高度的一半
        button_height = self.layout().itemAt(1).itemAt(0).widget().height()
        font_size = button_height // 2
        # 设置按钮文本的样式表
        button_style = "QPushButton { font-size: %dpx; text-align: center; }" % font_size
        print(font_size)
        self.setStyleSheet(button_style)

    def suitSize(self):
        font = self.result_display.font()
        font_metrics = QFontMetrics(font)
        text_width = font_metrics.width(self.result_display.text())
        available_width = self.result_display.width()
        if text_width > available_width:
            # 计算适合的字体大小，并缩小字体
            font_size = font.pointSizeF()
            while text_width > available_width and font_size > 1:
                font_size -= 0.5
                font.setPointSizeF(font_size)
                font_metrics = QFontMetrics(font)
                text_width = font_metrics.width(self.result_display.text())
            self.result_display.setFont(font)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 根据QLineEdit的宽度和文本内容来调整字体大小
        font = self.result_display.font()
        font_size = int(self.result_display.height() * 0.5)
        font.setPointSize(font_size)
        self.result_display.setFont(font)
        self.suitSize()
        self.setButtonStyle()
        print(self.window().height())
    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #
    #     # 根据QLineEdit的高度设置字体大小
    #     print(self.result_display.height())
    #     font_size = int(self.result_display.height()*0.5)
    #     font = self.result_display.font()
    #     font.setPointSize(font_size)
    #     print(font_size)
    #     self.result_display.setFont(font)
    #     self.result_display.font().setBold(True)
    def handle_button_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.result_display.clear()
        elif text == 'CE':
            current_text = self.result_display.text()
            self.result_display.setText(current_text[:-1])
        elif text == '=':
            expression = self.result_display.text()
            try:
                result = eval(expression)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText('Error')
        else:

            current_text = self.result_display.text()
            if current_text == '0':
                self.result_display.setText(text)
            else:
                self.result_display.setText(current_text + text)
            self.suitSize()


if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
