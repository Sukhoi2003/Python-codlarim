try:
    with open('product_material.txt', 'r') as f:
        data = f.read()
except FileExistsError:
    print("Bunday fayl yo'q")
else:
    data = data.split('\n')[:-1]

    for line in data:
        line = line.split(',')
        if line[-1] == "false" or float(line[3][1:]) < 1000:
            print(line[2])