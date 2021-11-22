from PyQt5 import QtCore, QtWidgets
from sys import argv, exit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 303)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 321, 221))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Aller"))


class Main(Ui_Dialog, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = -1
        self.y = -1
        self.m = 0
        self.setMouseTracking(True)
        self.color = ['Yellow']

    def logic(self, hope):
        self.x = hope.x()
        self.y = hope.y()
        if hope.button() == Qt.LeftButton:
            self.m = 1
        elif hope.button() == Qt.RightButton:
            self.m = -1
        self.update()

    def paintEvent(self, hope):
        cher = QPainter()
        cher.begin(self)
        self.drawing(cher)
        cher.end()

    def drawing(self, cher):
        if self.x > -1 and self.y > -1 and self.m == -1:
            cher.setBrush(QColor(choice(self.color)))
            a = randint(1, 100)
            cher.drawEllipse(self.x, self.y, a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
