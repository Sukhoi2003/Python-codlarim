def isUpper(n) -> bool:
    for i in range(2, n//2+1):
        if not n%i:
            return False

    return True

print(isUpper(5))