n, sum = input('n= '), 0
n = int(n[:5])
print(n)
while n > 0:
    sum+=n%10
    n//=10
print(sum)