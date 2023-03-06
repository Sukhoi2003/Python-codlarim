m = int(input("m= "))
n = list()
for i in range(m):
    n.append(input("n= "))


n = list(map(lambda i : int(i) if i.isnumeric() or i[1:].isnumeric() and i[0] == "-" else 0, n))

print(n)