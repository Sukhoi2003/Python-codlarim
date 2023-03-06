try:
    with open("book.txt", 'r') as f:
    data = f.read()
except FileNotFoundError:
    print("Bunday fayl yo'q")
else:
    data = data.split("\n")[-1]

    for line data:
        line = line.split(",")
        print(*line)
