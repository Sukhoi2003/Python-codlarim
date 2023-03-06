class Bino:

    def __init__(self, height, color):
        self.balandligi = height
        self.rangi = color

b1 = Bino(100, "Qora")

b2 = Bino(42, "Yashil")

b3 = Bino(51, "Sariq")

b4 = Bino(23, "Ko'k")

b5 = Bino(200, "Pushti")

for i in [b1, b2, b3, b4, b5]:
    if i.balandligi > 50:
        print(i.rangi)