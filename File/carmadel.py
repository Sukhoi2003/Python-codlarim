def car(data):
    n,m=0,0
    for i in data:
        i = i.split(',')
        if i[3] == 'Male':
            n += 1
        if i[3] == "Female":
            m += 1
    return 100 - (m*100//n)
try:
    n = 0
    m = 0
    with open('car_model.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("Bunday fayl yo'q")
else:
    data = data.split("\n")[:-1]
    print(car(data))
