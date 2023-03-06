import sys

from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()
    label = QtWidgets.QLabel(win)
    btn = QtWidgets.QPushButton(win)
    edit = QtWidgets.QLineEdit(win)

    win.setWindowTitle("Birinchi dasturim")
    win.setGeometry(1700, 1500, 400, 400)

    label.setText("Ismingizni kiriting")
    btn.setText("Yuborish")

    label.move(100, 80)
    edit.move(100, 100)
    btn.move(100, 130)

    win.show()
    app.exec_()


window()