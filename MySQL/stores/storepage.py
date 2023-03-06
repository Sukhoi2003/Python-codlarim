import sys 

from databasa import *

from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QWidget,
    QPushButton,
    QTableWidget,
    QRadioButton
)

class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Store Page")
        self.vbox1 = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()

                
        self.led1 = QLineEdit()
        self.led2 = QLineEdit()
        self.led3 = QLineEdit()

        self.ledbtn = QPushButton("Add product")

        self.table = QTableWidget()
        self.table.setColumnCount(3)


        self.seline = QLineEdit()
        self.search = QPushButton("Search")
        self.allproduct = QPushButton("All product")

        self.prodradio = QRadioButton("Product")
        self.priceradio = QRadioButton("Price")
        self.amountradio = QRadioButton("Amount")

        self.prolabel = QLabel("Product")
        self.proline = QLineEdit()
        self.deletbtn = QPushButton("DELETE")


        self.hbox1.addWidget(self.led1)
        self.hbox1.addWidget(self.led2)
        self.hbox1.addWidget(self.led3)
        self.hbox1.addWidget(self.ledbtn)

       


        self.hbox3.addWidget(self.table)

        self.hbox4.addWidget(self.seline)
        self.hbox4.addWidget(self.search)
        self.hbox4.addWidget(self.allproduct)

        self.hbox5.addWidget(self.prodradio)
        self.hbox5.addWidget(self.priceradio)
        self.hbox5.addWidget(self.amountradio)

        self.hbox6.addWidget(self.prolabel)
        self.hbox6.addWidget(self.proline)
        self.hbox6.addWidget(self.deletbtn)

        self.vbox1.addLayout(self.hbox1)
        self.vbox1.addLayout(self.hbox2)
        self.vbox1.addLayout(self.hbox3)
        self.vbox1.addLayout(self.hbox4)
        self.vbox1.addLayout(self.hbox5)
        self.vbox1.addLayout(self.hbox6)
        
        self.ledbtn.clicked.connect(self.add)

        self.setLayout(self.vbox1)




    def add(self):
        self.addd = Core()
        self.addd.insertUser(self.led1.text(), self.led2.text(), self.led3.text())





app = QApplication([])
win = Main()
win.show()
sys.exit(app.exec_())