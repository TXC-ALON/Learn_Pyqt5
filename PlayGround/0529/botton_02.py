from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QStyleFactory


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 QPushButton 对象
        self.btn = QPushButton('Button', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)

    def enterEvent(self, event):
        # 鼠标进入按钮区域时，显示 tooltip
        self.btn.setToolTip('Mouse is hover over me')

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion')) # 更改全局样式为 Fusion 风格
    ex = Example()
    ex.show()
    app.exec_()
