try:
    with open('car_model.txt', 'r') as f:
        data = f.read().split("\n")[1:-1]
except FileNotFoundError:
    print("Bunday fayl yo'q")
else:
    lst = list()
    car_count = dict()
    for line in data:
        l = line.split(",")
        try:
            car_count.get(l[4])
            car_count[l[4]]=car_count[l[4]] + 1
        except:
            car_count[l[4]] = 1

        lst.append([l[4], l[7]])
    maxcount = sorted(car_count.values(), reverse=True)[0]
    for k, v in car_count.items():
        if v == maxcount:
            print(k, v), f, seed, []