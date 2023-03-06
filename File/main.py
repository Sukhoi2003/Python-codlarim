try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileExistsError:
    print("Bunday fayl yo'q")
else:
    data = data.split('\n')[:-1]

    for line in data:
        line = line.split(',')
        if line[2] == "Male":
            print(line[0],line[1],line[-1])