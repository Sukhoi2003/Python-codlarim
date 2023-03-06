Dastur = {'html', 'sess', 'java', 'python', 'golang'}
SoftLen = set()

for i in Dastur:
    SoftLen.update(range(len(i)))
print(SoftLen)
