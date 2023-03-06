try:
    with open('product_material.txt', 'r') as f:
        product_material = f.read()
except FileNotFoundError:
    print("Bunday fayl yo'q")
else:
    product_material = product_material.split('\n')[:-1]

    for line in product_material:
        line = line.split(',')
        if 500 < float(line[3][1:]) < 1000 or line[-1] == 'true':
            print(line[0], line[2])
