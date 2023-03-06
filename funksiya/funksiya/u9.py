#def add(n: list, m: int):
#    nums = list()
#    for i in t:
#        nums.append(i*m)
#    return nums
#


#print(add(t, m))

def add_update(n: list, m: int):
    for i in range(len(n)):
        n[i] *= m
        
    return n
t = [1, 2, 3, 4, 5]
m = 5

print(add_update(t, m))