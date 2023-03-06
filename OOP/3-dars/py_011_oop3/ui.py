from core import Student
from db import File

ism = input('Ism : ')
guruh = input('Guruh : ')
kurs = input('Kurs: ')

s1 = Student(ism, guruh, kurs)
print(s1)

f = File()
f.insert(s1)

for student in f.getStudents():
    print(student)