i = c=0

for i in range(100):
    if i % 10 == 3 or i // 10 == 3 or i == 3:
        c+=1
        print(i, end=' ')
        print()
print(f'Soni {c} ta ')

