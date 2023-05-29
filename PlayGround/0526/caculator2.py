from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, \
    QSpacerItem, QSizePolicy
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
        fontsize = 45
        # # 创建一个 QLineEdit 用于显示计算结果
        # self.result_display = QLineEdit('0')
        # self.result_display.setMinimumHeight(fontsize)
        # #self.result_display.setStyleSheet("QLineEdit { font-size: 55px; }")
        # font = self.result_display.font()
        # font.setPointSize(fontsize)  # 设置字体大小
        # font.setBold(True)  # 设置字体为粗体
        # self.result_display.setFont(font)
        # self.result_display.setAlignment(Qt.AlignRight)
        # self.result_display.setReadOnly(True)

        # 创建一个 QLineEdit 用于显示计算结果
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setFixedSize(200, 40)  # 设置固定的宽度和高度
        self.result_display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 设置文本从右往左增长并垂直居中
        self.result_display.setStyleSheet("QLineEdit { font-size: 40px; }")  # 设置数字的字体大小

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
        grid_layout.addWidget(self.result_display, 0, 0, 1, 4)
        grid_layout.setSpacing(5)  # 设置按钮之间的间距

        # 将按键添加到网格布局
        row, col = 1, 0
        for button in buttons:
            button_obj = PushButton(button)
            grid_layout.addWidget(button_obj, row, col)
            button_obj.clicked.connect(self.handle_button_click)
            col += 1
            if col > 3:
                col = 0
                row += 1

         # 设置主布局
        #spacer_item = QSpacerItem(20, 40, 10, QSizePolicy.Expanding)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_display)
        #main_layout.addItem(spacer_item)  # 添加可变长度的间隔
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

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


if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
