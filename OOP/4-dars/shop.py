from datetime import datetime
from uuid import uuid4

class Shop:
    def __init__(self, name, passwort, balans, product, incomeproduct):
        self.name = name
        self.password = passwort
        self.balans = balans
        self.product = product
        self.incomproduct = incomeproduct

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getBalans(self):
        return self.balans

    def getProduct(self):
        return self.product

    def getIncomproduct(self):
        return self.incomproduct


    def setNaame(self, newname):
        self.name = newname

    def setPasword(self, newPaswort):
        self.password = newPaswort

    def setNalans(self, newbalans):
        self.balans = newbalans

    def setProduct(self, newproduct):
        self.product = newproduct

    def setIncomproduct(self, newincomproduct):
        self.incomproduct = newincomproduct

havas = ("laptop" "flash", "sausage", "meat", "chicken")
s = Shop("Havas", 1245, 100000, havas, "lapota")
print(s)