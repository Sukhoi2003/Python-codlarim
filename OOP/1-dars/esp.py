class Student:
    def __init__(self, fname, lname, gpa) -> None:
        self.fname = fname
        self.lname = lname
        self.gpa = gpa


    def __str__(self) -> str:
        return f"{self.fname} {self.lname} {self.gpa}"

    def getGpa(self):
        return self.gpa

    def setGpa(self, gpa):
        self.gpa = gpa

    def getFname(self):
        return self.fname

s1 = Student("Aziz", "Sherbpev", 3.2)
s2 = Student("Aziza", "Fras", 33.1)
s3 = Student("Manzura", "Sherbpeva", 23.2)

students = [s1, s2, s3]
min = students[0]
for i in students:
    if i.getGpa() > min.getGpa():
        min = i

print(min.getFname())