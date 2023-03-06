class Book:

    def __init__(self,name, authers, price, ganre, page) -> None:
        self.name = name
        self.mualliflar = authers
        self.narx = price
        self.janri = ganre
        self.sahifa = page

    def getFull_Info(self) -> str:
        return f"""
            Object
        Name of object : {self.name}
        Muallifi : {self.mualliflar}
        Narxi : {self.narx}
        Janri : {self.janri}
        Sahifa: {self.sahifa}
        """

    def change_Price(self, price):
        self.narx=price

b = Book("Robinzon Kruzo,", "Esimda yo'q", "1000$", "Sarguzash", "150 sahifa")
print(b.getFull_Info())

b.change_Price(20000000)
print(b.getFull_Info())
