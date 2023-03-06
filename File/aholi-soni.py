try:
    with open('aholi.txt', 'r') as f:
        aholi = f.read()
except FileExistsError:
    print("Bunday fayl yo'q")
else:
    aholi = aholi.split('\n')[:-1]


    for line in aholi:
        line = line.split(',')
        if line[1] > "1000000":
            print(*line)