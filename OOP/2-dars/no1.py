class Person:
    def __init__(self, name, age, salary, country) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.country = country

    def __str__(self) -> str:
        return f"""
|----------------------|
    Name: {self.name}
    Age: {self.age}
    Salary: {self.salary}
    Country: {self.country}
-------------------------"""


class Coach(Person):
    def __init__(self, name, age, salary, country, exp) -> None:
        super().__init__(name, age, salary, country)
        self.exp = exp

    def __str__(self) -> str:
        return f"""{super().__str__()}
    Exp: {self.exp}
        """


class Player(Person):
    def __init__(self, name, age, salary, country, number, position) -> None:
        super().__init__(name, age, salary, country)
        self.number = number
        self.position = position

    def __str__(self) -> str:
        return f"""{super().__str__()}
    Number: {self.number}
    Position: {self.position}
-------------------------
        """


class Club:
    def __init__(self, name = '' , stadium = '', balans = 0) -> None:
        self.name = name
        self.stadium = stadium
        self.balans = balans
        self.coach = ''
        self.players = list()

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setCoach(self, newCoach):
        self.coach = newCoach

    def appendPlayer(self, newPlay):
        self.players.append(newPlay)

    def setClub(self, newClub):
        self.name = newClub

    def getClub(self):
        return self.name

    def getAllPlayers(self):
        for player in self.players:
            print(player)

    def bolganMetod(self):
        print(*self.players)

    def FullInfo(self):
        print(self.getName())
        print(self.coach)
        self.getAllPlayers()

c1 = Club()

p1 = Player("Eldor", 27, 15000000, 'Uzbekistan', 14, 'Forword')
p2 = Player("Odil", 39, 15000, 'Uzbekistan', 9, 'Forword')
p3 = Player("Messi", 35, 1000, 'Argentina', 10, 'Forword')
p4 = Player("Ronaldo", 37, 200000000, 'Portugal', 7, 'Forword')

coach = Coach('Babayan', 55, 5600, 'Armaniya', 12)
c1.setName("Taxtakor")
c1.setCoach(coach)

c1.appendPlayer(p1)
c1.appendPlayer(p2)
c1.appendPlayer(p3)
c1.appendPlayer(p4)

# c1.getAllPlayers()
#c1.bolganMetod()
c1.FullInfo()