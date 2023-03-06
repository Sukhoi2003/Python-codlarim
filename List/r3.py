dar = [1, 4, 5, 3, 9, 3, 2]
ar = dar.copy()

for i in range(len(dar)):
    if i%2:
        dar[i] = dar[i]**2
    else:
         dar[i] = dar[i]**3
son  = dar.copy()
print(ar)
print(dar)
