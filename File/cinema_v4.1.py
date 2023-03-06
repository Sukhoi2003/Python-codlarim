try:
    with open("cinema.txt", "r") as f:
        f = f.read()
except FileNotFoundError:
    print("Bunday fayl topilmadi")
else:
    n = int(input("Film vaqtini kiritng>>> "))
    f = f.split('\n')[:-1]
    for linya in f:
        linya=linya.split(',')
        if int(linya[-1][:-3])>n:
            print(*linya)