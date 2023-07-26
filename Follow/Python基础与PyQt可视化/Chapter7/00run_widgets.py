import sys  #Demo7_13.py
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

import Stu7_3  as student #导入student.py文件

class QmyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = student.Ui_Form()
        self.ui.setupUi(self)
        self.__count = 0
        self.__score = list()
    @pyqtSlot()
    def on_btnCalculate_clicked(self):
        s = self.ui.chinese.value()+self.ui.math.value()+self.ui.english.value()
        print("on_btnCalculate_clicked")
        print(s)
        self.ui.total.setText(str(s))
        template = "{:.1f}".format(s/3)
        self.ui.average.setText(template)

        self.__count = self.__count + 1
        temp = list()
        temp.append(self.__count)
        temp.append(self.ui.chinese.value())
        temp.append(self.ui.math.value())
        temp.append(self.ui.english.value())
        temp.append(s)
        temp.append(float(template))
        self.__score.append(temp)
    @pyqtSlot()
    def on_btnSave_clicked(self):
        template = "{}:语文{} 数学{} 英语{} 总成绩{} 平均分{}\n"  #定义文本模板
        try:
            fp = open("./student_score.txt",'a+',encoding='UTF-8')  #打开文件
        except:
            print("保存文件失败")
        else:
            for i in self.__score:
                score = template.format(i[0],i[1],i[2],i[3],i[4],i[5])  #格式化字符串
                fp.write(score)   #往文件中写入数据
            fp.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = QmyWidget()
    myWindow.show()
    n = app.exec()
    sys.exit(n)
