class Transport:
    def __init__(self, Brand, Model, Color):
        self.brendi = Brand
        self.madeli = Model
        self.rangi = Color

    def GetInfo(self) -> str:
        return f"""
        \+++Info+++/
    Brendi : {self.brendi}
    Madeli : {self.madeli}
    Rangi : {self.rangi}
        """

full = Transport("Gm", "Damas", "Oq")
print(full.GetInfo())

class Car(Transport):
    def __init__(self, Brand, Model, Color, SetSpeed, SetSeatCount):
        super().__init__(Brand, Model, Color)
        self.tezlik = SetSpeed
        self.orindiqsoni = SetSeatCount

    def GetInfo2(self) -> str:
        return f"""
        Car
    {super().GetInfo()}
    Tezligi : {self.tezlik}
    O'rindiqlari soni : {self.orindiqsoni}
    """

full = Car("Gm", "Damas", "Oq","140m/h", "6 ta")
print(full.GetInfo2())

class Truck(Transport):
    def __init__(self, Brand, Model, Color, WeightCapacity):
        super().__init__(Brand, Model, Color)
        self.yukkotaraolishi = WeightCapacity

    def GetInfo3(self) -> str:
        return f"""
        Truck
        \+++Info+++/
    {super().GetInfo()}
    Yuk ko'tara olishi : {self.yukkotaraolishi}
"""
full = Truck("Gm", "Damas", "Oq", "150 tonna")
print(full.GetInfo3())

