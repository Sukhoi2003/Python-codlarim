from core import Student

class File:
    def insert(self, std : Student):
        print(type(std), std)
        with open('students.txt', 'a') as f:
            f.write(str(std))
        

    def getStudents(self):
        with open('students.txt') as f:
            data = f.read().split('\n')[:-1]
        return list(map(lambda line: line.split(), data))

