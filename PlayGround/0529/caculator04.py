from PyQt5.QtGui import QFontMetrics, QPalette, QColor
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
        self.setStyleSheet('Calculator{background:white}')
        self.setWindowTitle("Calculator")
        self.setMinimumHeight(560)  # 设置窗口的最小高度为500像素
        self.setMinimumWidth(300)  # 设置窗口的最小宽度为300像素
        self.resize(400, 600)  # 设置默认宽度和高度
        # 创建一个 QLineEdit 用于显示计算结果
        self.result_display = QLineEdit('0')

        # 创建按键，并为数字、运算符、括号和等号分组 6*4
        buttons = [
            {'text': '%', 'group': '1'}, {'text': 'CE', 'group': '1'}, {'text': 'C', 'group': '1'},
            {'text': 'Del', 'group': '1'},
            {'text': '1/x', 'group': '2'}, {'text': 'x^2', 'group': '2'}, {'text': '√(x)', 'group': '2'},
            {'text': '/', 'group': '2'},
            {'text': '7', 'group': '3'}, {'text': '8', 'group': '3'}, {'text': '9', 'group': '3'},
            {'text': '*', 'group': '3'},
            {'text': '4', 'group': '4'}, {'text': '5', 'group': '4'}, {'text': '6', 'group': '4'},
            {'text': '-', 'group': '4'},
            {'text': '1', 'group': '5'}, {'text': '2', 'group': '5'}, {'text': '3', 'group': '5'},
            {'text': '+', 'group': '5'},
            {'text': '+/-', 'group': '6'}, {'text': '0', 'group': '6'}, {'text': '.', 'group': '6'},
            {'text': '=', 'group': '6'},
        ]

        # 创建按钮网格布局
        grid_layout = QGridLayout()
        grid_layout.setSpacing(5)  # 设置按钮之间的间距

        # 将按键添加到网格布局
        group_dict = {}
        col = 0
        row = 0
        for button in buttons:
            button_obj = PushButton(button['text'])
            grid_layout.addWidget(button_obj, row, col)
            button_obj.clicked.connect(self.handle_button_click)
            fontsize = button_obj.height() // 3
            group = button['group']
            if group not in group_dict:
                group_dict[group] = []
            group_dict[group].append(button_obj)
            if button['group'] < '4':
                button_obj.setStyleSheet("PushButton {{ font-size: {0}px; text-align: center;"
                                     "background-color: rgb(250, 250, 250); border-radius: 5px;}}".format(fontsize))  # 设置按钮文本的字体大小和居中对齐
            else:
                button_obj.setStyleSheet("PushButton {{ font-size: {0}px; text-align: center;"
                                         "background-color: rgb(0, 250, 250); border-radius: 5px;}}".format(
                    fontsize))  # 设置按钮文本的字体大小和居中对齐

            col += 1
            if col > 3:
                col = 0
                row += 1

        # 为每个按钮组设置背景颜色


        # 设置主布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_display)
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

        # 设置控件的大小策略

        self.result_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置QLineEdit水平方向自动拉伸，垂直方向固定大小
        self.result_display.setMinimumHeight(30)  # 设置最小高度为30px
        self.result_display.setMaximumHeight(80)  # 设置最小高度为30px

        self.result_display.setFixedHeight(self.result_display.height())
        self.result_display.fontMetrics()
        text_height = self.result_display.fontMetrics().height()
        self.result_display.setFixedHeight(self.result_display.height() - self.result_display.height() % text_height)
        self.result_display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        for i in range(grid_layout.count()):
            widget = grid_layout.itemAt(i).widget()
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置按钮自动拉伸

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

        # 根据QLineEdit的高度设置字体大小
        font_size = int(self.result_display.height() * 0.5)
        font = self.result_display.font()
        font.setPointSize(font_size)
        self.result_display.setFont(font)
        self.suitSize()

        # 调整按钮文本大小
        for i in range(self.layout().itemAt(1).count()):
            widget = self.layout().itemAt(1).itemAt(i).widget()
            fontsize = widget.height() // 3
            widget.setStyleSheet("QPushButton {{ font-size: {0}px; text-align: center;"
                                 "background-color: rgb(250, 250, 250); border-radius: 5px;}}".format(fontsize))
            # 为每个按钮组设置背景颜色

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
    app.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    calculator = Calculator()
    calculator.show()
    app.exec()
