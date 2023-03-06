with open("data.txt", "r") as f:
    data = f.read()
    data = data.split("\n")[:-1]
    sol = open("salom.txt", "a")
    for line in data:
        line = line.split(",")
        if line[-1] == 'Russia':
            print(line)
            sol.write(f'{line}\n')
    sol.close()