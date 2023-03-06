list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4,  6, 8]

list3 = list(filter(lambda i : i not in list2, list1))
print(list3)