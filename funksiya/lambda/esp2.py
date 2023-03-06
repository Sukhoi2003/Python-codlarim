lst = ['Salom', 'Reptiliya', 'Ermac', 'Smoke']

x = lambda k : k[0]



for i in range(len(lst)):
    lst[i] = x(lst[i])

print(lst)