class Book:

    def __init__(self, name, authers, price, ganre, page) -> None:
        self.ism = name
        self.muallif = authers
        self.narx = price
        self.janri = ganre
        self.sahifa = page
    
    def getaFull_info(self) -> str:
        return f"""
            Object
        name of book : {self.ism}
        Muallifi : {self.muallif}
        Narxi : {self.narx}
        Janri : {self.janri}
        Sahifa : {self.sahifa}
        """

    def changePrice(self, price):
        self.narx = price

    def changeGanre(self, ganre):
        self.janri = ganre

b = Book("Robinzon Kuruzo", "Esimda yuq", "100$", "Sarguzash", "160")
print(b.getaFull_info ())

b.changePrice(10000)
print(b.getaFull_info())

b.changeGanre("Sayohat")
print(b.getaFull_info())