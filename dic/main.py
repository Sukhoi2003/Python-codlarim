from random import random

a = random(1, 500)
b = random(1, 500)

c = int(input('{} + {} = '.format(a, b)))

if c == (a + b):
    print("To'g'ri")
else:
    print("xato")