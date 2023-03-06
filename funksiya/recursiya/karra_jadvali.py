def info(n, i):
    print(f'{n} * {i} = {n*i}')
    if i < 9:
        info(n, i+1)

info(5, 1)