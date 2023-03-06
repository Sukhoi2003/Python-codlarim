class Transport:
    def __init__(self, Brand, Model, Color):
        self.brendi = Brand
        self.madeli = Model
        self.rangi = Color

    def GetInfo(self) -> str:
        return f"""
            Info
        Brendi : {self.brendi}
        Madeli : {self.madeli}
        Rangi : {self.rangi}
        """
m = Transport("Lada", "Jiguli", "Qop-qora")
print(m.GetInfo())