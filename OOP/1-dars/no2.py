class Person:
    def __init__(self, name, age, phone) -> None:
        self.n = name
        self.a = age
        self.ph = phone
    
    def getFullInfo(self):
        return f""""{self.n} {self} {self.ph}"""

class Hodim(Person):
    def __init__(self, name, age, phone, status) -> None:
        super().__init__(name, age, phone)
        self.s = status

    def giveCredit(self):
        return "Yoq kredit"

    def getFullInfo(self):
        return f'{super().getFullInfo()} {self.s}'

class Mijoz(Person):
    def __init__(self, name, age, phone) -> None:
        super().__init__(name, age, phone)
        self.credit_sum = 100000

    def getCredit(self):
        return '10000000000 kredit ber'


if __name__ == '__name__':
    p1 = Person('Aziz', 37, +998931307015)
    h1 = Hodim('Boqivoy', 27, +998955445555)
    m1 = Mijoz("Qo'zivoy", 23, +998965214785)


    print(p1.getFullInfo())
    print(h1.getFullInfo())
    print(m1.getCredit())
    print(h1.giveCredit())
