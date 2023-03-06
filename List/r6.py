n = [
[5, 3, 7], 
[1, 40, 9], 
[2, 8, 6]
]

m = 0

for i in range(len(n)):
    if m < sum(n[i]):
        m = (sum(n[i]))
print(m)
