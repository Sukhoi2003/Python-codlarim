from math import pi

class Square:
    def __init__(self, a) -> None:
        self.a = a

    def getArea(self):
        return self.a ** 2

class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b
class Circle:
    def __init__(self, r) -> None:
        self.r = r
    def getArea(self):
        return (self.r ** 2) * pi


class Kub:
    def __init__(self, a):
        self.a = a
    def getArea(self):
        return 6*(self.a**2)

s1 = Square(4)
s2 = Square(7)

r1 = Rectangle(3, 5)
r2 = Rectangle(2, 4)

c1 = Circle(3.4)
c2 = Circle(10)

k1 = Kub(2)
k2 = Kub(7)

lst = [s1, s2, r1, r2, c1, c2, k1, k2]

for i in lst:
    print(i.getArea())