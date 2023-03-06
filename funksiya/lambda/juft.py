lst = [1, 2, 43, 44, 54, 434, 23, 3, 4]

thor = list(filter(lambda i : not i%2, lst))
print(thor)