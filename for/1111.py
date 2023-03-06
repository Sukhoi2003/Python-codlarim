n, total = int(input('n= ')), '1'
i = 2
summa = '1'
while n >= i:
    total += ' + '
    total += '1' * i
    summa += str(i)
    print(total, summa, sep=' = ')
    i+=1

