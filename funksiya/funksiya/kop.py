#def temp(item : list, n : int):
#    nums = list()
#    for i in item:
#        nums.append(i*n)
#
#    return nums
#
#t = [1, 2, 3, 4, 5]
#n = int(input('n= '))
#print(temp(t,n))

def temp(item : list, n = 1):
    for i in range(len(item)):
        item[i] *= n

    return item

t = [1,2,3,4,5]
n = 5
print(temp(n = n, item = t))
