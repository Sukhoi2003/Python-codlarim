def fact(n):
    if n == 2:
        return 2
    return n * fact(n-1)




print(fact(int(input('n= '))))