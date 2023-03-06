from math import sqrt

def isPrime(n: int) -> bool:
    if n in [2,3]:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1):
        if not n % i:
            return False

    return True

print(isPrime(739))


#def isPrime(n: int) -> bool:
#    for i in range(2, n//2+1):
#        if not n % i:
#            return False
#            
#    return True
#
#print(isPrime(int(input('n=> '))))
#