lst = [23, 43, 12, 5, 4, 54, 3]
lst2 = ['23', '43', '92', '2']

print(lst)

lst = sorted(list(map(lambda a: str(a), lst)), reverse=True)
print(lst)
