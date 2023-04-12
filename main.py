"""
作者：不看盘的量化交易员
日期：2023年04月4日
"""
import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from compute import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绑定信号处理函数
        self.bind()

    def bind(self):
        self.pushButton.clicked.connect(lambda: self.getchar('0'))
        self.pushButton_1.clicked.connect(lambda: self.getchar('1'))
        self.pushButton_2.clicked.connect(lambda: self.getchar('2'))
        self.pushButton_3.clicked.connect(lambda: self.getchar('3'))
        self.pushButton_4.clicked.connect(lambda: self.getchar('4'))
        self.pushButton_5.clicked.connect(lambda: self.getchar('5'))
        self.pushButton_6.clicked.connect(lambda: self.getchar('6'))
        self.pushButton_7.clicked.connect(lambda: self.getchar('7'))
        self.pushButton_8.clicked.connect(lambda: self.getchar('8'))
        self.pushButton_9.clicked.connect(lambda: self.getchar('9'))
        self.pushButton_10.clicked.connect(self.lineEdit.clear)
        # self.pushButton_11.clicked.connect(lambda: self.getchar(''))
        self.pushButton_12.clicked.connect(lambda: self.getchar('+'))
        self.pushButton_13.clicked.connect(lambda: self.getchar('-'))
        self.pushButton_14.clicked.connect(lambda: self.getchar('*'))
        self.pushButton_15.clicked.connect(lambda: self.getchar('/'))
        self.pushButton_16.clicked.connect(self.equal)

    def getchar(self, ch):
        self.lineEdit.setText(self.lineEdit.text() + ch)

    def equal(self):
        self.lineEdit.setText(str(eval(self.lineEdit.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec()
