from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        # title
        self.title = QLabel()
        self.title.setText("血型分析器")
        self.title.setAlignment(Qt.AlignCenter)
        # text.ba
        self.tba = QLabel()
        self.tba.setText("你爸血型")
        # cb.ba
        self.cba = QComboBox()
        self.cba.addItems(["A","B","AB","O"])
        # cb.nm
        self.cnm = QComboBox()
        self.cnm.addItems(["A","B","AB","O"])
        # self.m
        self.m = QLabel()
        self.m.setText("你妈血型")
        # sta.btn
        self.stabtn = QPushButton()
        self.stabtn.setText("开始分析")

        # layout
        self.main = QVBoxLayout()
        self.babamama = QHBoxLayout()
        self.lba = QVBoxLayout()
        self.lnm = QVBoxLayout()

        # addwidget and addlayout
        self.lba.addWidget(self.tba)
        self.lba.addWidget(self.cba)
        self.lnm.addWidget(self.m)
        self.lnm.addWidget(self.cnm)
        self.babamama.addLayout(self.lba)
        self.babamama.addLayout(self.lnm)

        self.main.addWidget(self.title)
        self.main.addLayout(self.babamama)
        self.main.addWidget(self.stabtn)

        # window
        self.widgets = QWidget()
        self.widgets.setLayout(self.main)
        self.setCentralWidget(self.widgets)
        self.setWindowTitle("血型分析器")
        self.show()
        # trc
        self.stabtn.pressed.connect(self.stabtnc)
        # tr
    def stabtnc(self):
        self.bax = self.cba.currentText()
        self.mx = self.cnm.currentText()
        print("[info] callback babox combox",self.bax," nmsl combox",self.mx)
        if(self.bax == "A" and self.mx == "A"):
            self.msgback = "你的血型是： 2A 型"
        elif(self.bax == "B" and self.mx == "B"):
            self.msgback = "你的血型是： 2B 型"
        elif(self.bax == "AB" and self.mx == "AB"):
            self.msgback = "你的血型是： 2AB 型"
        elif(self.bax == "O" and self.mx == "O"):
            self.msgback = "你的血型是： 2O 型"
        else:
            self.close()
        self.msg = QMessageBox()
        self.msg.setText("恭喜你！！")
        self.msg.setInformativeText(self.msgback)
        self.msg.setWindowTitle("结果")
        self.msg.setStandardButtons(QMessageBox.Ok)
        revecel = self.msg.exec_()
def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
        