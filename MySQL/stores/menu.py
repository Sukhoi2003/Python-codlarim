from PyQt5.QtWidgets import *
from store import *
from databasa import *


class Menu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.addprod)




    def addprod(self):
        self.yoz = Core()
        self.yoz.insertUser(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text())
        self.ui.tableWidget.setItem(0,0,QTableWidgetItem(self.ui.lineEdit.text()))
        self.ui.tableWidget.setItem(0,1,QTableWidgetItem(self.ui.lineEdit_2.text()))
        self.ui.tableWidget.setItem(0,2,QTableWidgetItem(self.ui.lineEdit_3.text()))
    

app = QApplication([])
win = Menu()
win.show()
exit(app.exec_())