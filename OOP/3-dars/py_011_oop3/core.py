class Student:
    def __init__(self, ism, guruh, kurs) -> None:
        self.ism = ism
        self.guruh = guruh
        self.kurs = kurs

    def __str__(self) -> str:
        return f'{self.ism} {self.guruh} {self.kurs}\n'