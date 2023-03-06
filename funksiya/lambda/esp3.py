#x = lambda a : a * 10
#
#print(x(10))

def func(n):
    return lambda a : a * n

mult = func(2)
y = func(3)

print(mult(10))
print(y(10))