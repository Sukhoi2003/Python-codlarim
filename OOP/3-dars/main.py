import os
from time import sleep


class User:
    def __init__(self, login='', password='') -> None:
        self.__login = login
        self.__password = password
        self.try_count = 3

    def getPassword(self):
        return self.__password

    def getLogin(self):
        return self.__login

    def setPassword(self, login, password, newPassword):
        self.try_count -= 1
        if self.checkNumberOfPossibilities():
            return 'Finish. Blocked Account.'

        if login != self.getLogin():
            return f'Invalid Login {login}'
        elif password != self.getPassword():
            return f'Invalid Password {password}'

        self.__password = newPassword
        self.try_count = 3

        return 'Chenged password'

    def setLogin(self, login, password, newLogin):
        self.try_count -= 1

        if self.checkNumberOfPossibilities():
            return 'Finish. Blocked Account.'

        if login != self.getLogin():
            return f'Invalid Login {login}'
        elif password != self.getPassword():
            return f'Invalid Password {password}'

        self.__login = newLogin
        self.try_count = 3

        return 'Chenged login'

    def checkNumberOfPossibilities(self):
        return not self.try_count


class Display:
    def show(self):
        os.system('clear')
        print('1. Show Login')
        print('2. Show Password')
        print('3. Change Login')
        print('4. Change Password')
        print('5. Exit')


u1 = User('muhammad_03', 'sukhoi')
display = Display()

while 1:
    display.show()
    n = int(input('>>> '))
    if n == 1:
        print(u1.getLogin())
    elif n == 2:
        print(u1.getPassword())
    elif n == 3:
        print(u1.setLogin(input('Enter login: '), input('Enter password: '), input('Enter new login: ')))
    elif n == 4:
        print(u1.setPassword(input('Enter login: '), input('Enter password: '), input('Enter new password: ')))
    elif n == 5:
        print('Bay bay')
        break
    sleep(5)

