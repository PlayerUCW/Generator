import sys
import random
from UI import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gen)

    def gen(self):
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        for i in range(5):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QtGui.QColor(r, g, b))
            d = random.randint(5, 200)
            x = random.randint(0, 400 - d)
            y = random.randint(0, 400 - d)
            qp.drawEllipse(x, y, d, d)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())