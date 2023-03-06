lst = [1,2,4,5,34,54,34]
try:
    n = int(input('indexni kiriting-> '))
    print(lst.pop(n))
except (IndexError, ValueError, NameError):
    print('Bunday index yoq')
