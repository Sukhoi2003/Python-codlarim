def addTen(n):
    return n+10

lst = [1, 2, 3, 4, 5, 6, 7]
#nums = list()
#
#for i in lst:
#    nums.append(addTen(i))
#
#print(nums)

nums = tuple(map(addTen, lst))
print(nums)