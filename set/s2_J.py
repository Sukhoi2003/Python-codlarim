SoftLen = {33, 212, 53, 32, 29, 21, 43}

max=0
for i in SoftLen:
    if max<i:
        max=i
print(max)
min = int()
for i in SoftLen:
    if min>i:
        min=i
print(min)


print(SoftLen)