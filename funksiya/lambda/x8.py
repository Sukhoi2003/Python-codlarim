n = [("V", 62), ("VI", 99), ("VII", 12)]

a = tuple(min(n, key=lambda i: i[1]))
m = tuple(max(n, key=lambda i: i[1]))
print(a[1], m[1])

