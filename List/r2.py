r = [
[2, 15, 4], 
[19, 24, 11], 
[7, 9, 5], 
[10, 3, 1]
]

for i in range(len(r)):
    for j in range(len(r[i])):
        if j%2:
            r[i][j] = r[i][j]**2
print(r)