class Rectangel:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def GetPrementre(self):
        return 2 * (self.a + self.b)
    def GetArea(self):
        return self.a * self.b

rect1 = Rectangel(2, 3)
print(rect1.GetPrementre())
print(rect1.GetArea())

