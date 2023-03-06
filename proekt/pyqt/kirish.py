import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout


class Register(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Registration")
        self.v_box = QVBoxLayout()
        self.h1_box = QHBoxLayout()
        self.h2_box = QHBoxLayout()
        self.h3_box = QHBoxLayout()
        self.h4_box = QHBoxLayout()
        self.h5_box = QHBoxLayout()

        self.save = QPushButton("Saqlash")
        self.save.clicked.connect(self.saqlash)

        self.ism = QLabel("Ism")
        self.fam = QLabel("Familya")
        self.login = QLabel("Login")
        self.parol = QLabel("Parol")

        self.ismga = QLineEdit()
        print(self.ismga.text())
        self.famga = QLineEdit()
        self.loginga = QLineEdit()
        self.parolga = QLineEdit()

        self.h1_box.addWidget(self.ism)
        self.h1_box.addWidget(self.ismga)

        self.h2_box.addWidget(self.fam)
        self.h2_box.addWidget(self.famga)

        self.h3_box.addWidget(self.login)
        self.h3_box.addWidget(self.loginga)

        self.h4_box.addWidget(self.parol)
        self.h4_box.addWidget(self.parolga)

        self.h5_box.addWidget(self.save)

        self.v_box.addLayout(self.h1_box)
        self.v_box.addLayout(self.h2_box)
        self.v_box.addLayout(self.h3_box)
        self.v_box.addLayout(self.h4_box)
        self.v_box.addLayout(self.h5_box)

        self.setLayout(self.v_box)


    def saqlash(self):
        with open("database.txt", "a") as f:
            f.write(self.ismga.text() + " ")
            f.write(self.famga.text() + " ")
            f.write(self.famga.text() + " ")
            f.write(self.parolga.text() + "\n")
            self.hide()
