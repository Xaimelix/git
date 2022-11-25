import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from random import randint
from git_ui import Ui_MainWindow


class A(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        a = ([randint(1, 500)] * 2)
        print(a)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPoint(400, 300), *a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = A()
    ex.show()
    sys.exit(app.exec())
