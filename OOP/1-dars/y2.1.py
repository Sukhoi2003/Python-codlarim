class Talaba:

    def __init__(self, name, surname, price) -> None:
        self.ism = name
        self.familya = surname
        self.baho = price



t1 = Talaba("Djo", "Bayden", 2)

t2 = Talaba("Vladim", "Putin", 5)

t3 = Talaba("Rishi", "Sunak", 3)

for i in [t1, t2, t3]:
    if i.baho==min(t1.baho,t2.baho,t3.baho):
        print(i.ism,i.familya)