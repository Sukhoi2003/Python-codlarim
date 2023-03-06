def arr(name: list):
    return tuple(sorted(name, reverse=True))


n = [12, 23, 34, 45, 54]
print(arr(n))