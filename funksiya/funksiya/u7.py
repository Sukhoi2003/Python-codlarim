def kv(lst):
    for i in range(len(lst)):
        lst[i]*=lst[i]
    return lst
a = int(input('n= '))
lst = []
for i in range(a):
    b = int(input('b= '))
    lst.append(b)
print(kv(lst))
