def Factarial(n):
    if n in [0,1] : return 1
    return n * Factarial(n-1)