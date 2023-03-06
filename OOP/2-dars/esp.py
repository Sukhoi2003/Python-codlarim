'''class Shaxs:
    """Shaxslar haqida ma'lumot"""#

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
  #      return yil - self.tyil

b = Shaxs("Mansur", "Aliyev", "Ac", 2003)
print(b.get_info())'''


class Person:

    def __init__(self, name, age, salary, country) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.country = country

class Coach(Person):
    def __init__(self, name, age, salary, country, exp) -> None:
        super().__init__(name, age, salary, country)
        self.exp = exp


class Player(Person):
    def __init__(self, name, age, salary, country, number, position) -> None:
        super().__init__(name, age, salary, country)
        self.number = number
        self.position = position


    

class Club:
    def __init__(self, name = '', station = '', balans = 0) -> None:
        self.name = name
        self.stadium = station
        self.balans = balans
        self.coach = Coach
        self.players = list()


    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setCoach(self, newCoach):
        self.coach = newCoach

    def appentPlayer(self, newPlayer):
        self.players.append(newPlayer)

c1 = Club()

p1 = Player("To'rayev", 33, 100, "Uzbekiston", 10, "Afsuski Forwort")
p2 = Player("Odil", 39, 1005, "Uzbekiston", 10, "Forwort")

coach = Coach("Babayan", 55, 5600, "Armaniston", 12)

c1.setCoach(coach)

c1.appentPlayer(p1)
c1.appentPlayer(p2)

print(c1.coach)

