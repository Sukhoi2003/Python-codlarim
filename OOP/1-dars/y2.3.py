class Notebook:

    def __init__(self, Company, Model, CPU, DDR, Price):
        self.firma = Company
        self.madel = Model
        self.protsessor = CPU
        self.ram = DDR
        self.narx = Price

    def nout(self) -> str:
        return f"""
        Info
    Firmasi : {self.firma}
    Madeli : {self.madel}
    Protsessori : {self.protsessor}
    RAM : {self.ram}
    Narxi : {self.narx}
    """

kom = Notebook("HP", "Victus", "intel cor i5", 8, "680$")
print(kom.nout())
