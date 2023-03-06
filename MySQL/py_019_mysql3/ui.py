import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit

from core import Core


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()
        self.setWindowTitle('Sign in')
        self._Init()


    def _Init(self):
        self.v_box = QVBoxLayout()
        self.h_box_login = QHBoxLayout()
        self.h_box_pwd = QHBoxLayout()
        self.h_box_comd = QHBoxLayout()

        self.login_label = QLabel('Login: ')
        self.pwd_label = QLabel('Password: ')

        self.login_edit = QLineEdit()
        self.pwd_edit = QLineEdit()

        self.login_edit.setPlaceholderText('Enter login...')

        self.btn_save = QPushButton('Save')
        self.btn_exit = QPushButton('Exit')

        self.btn_save.setStyleSheet("background-color: green; \
                                    color : white;")
        self.btn_exit.setStyleSheet("background-color: red;\
                                    color : white;")

        self.h_box_login.addWidget(self.login_label)
        self.h_box_login.addWidget(self.login_edit)

        self.h_box_pwd.addWidget(self.pwd_label)
        self.h_box_pwd.addWidget(self.pwd_edit)

        self.h_box_comd.addStretch()
        self.h_box_comd.addWidget(self.btn_exit)
        self.h_box_comd.addWidget(self.btn_save)

        self.v_box.addLayout(self.h_box_login)
        self.v_box.addLayout(self.h_box_pwd)
        self.v_box.addLayout(self.h_box_comd)

        self.btn_exit.clicked.connect(lambda : self.off_window('Exit'))
        self.btn_exit.setShortcut('Ctrl+N')

        self.btn_save.clicked.connect(lambda: self.save_user('ok'))
        self.btn_save.setShortcut('1')

        self.setLayout(self.v_box)

        self.show()

    def display_clear(self):
        self.login_edit.clear()
        self.pwd_edit.clear()

    def off_window(self, ok):
        print(ok)
        self.close()

    def save_user(self, ok):
        self.core.createUser(self.login_edit.text(),self.pwd_edit.text())
        self.display_clear()
        print(ok)

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())