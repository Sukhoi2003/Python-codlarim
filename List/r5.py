n = int(input('n= '))

num =  (5, -3, 4, -2, 1, -9, 8, -6, 7, 0, 4)

ls = list(num)
for i in num:
    if n in ls:
        ls.remove(n)
print(num)
lm = tuple(ls)
print(lm)