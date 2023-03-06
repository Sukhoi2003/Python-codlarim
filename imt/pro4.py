with open("text.txt", "r") as file:
    data = file.read()
data = data.split("\n")
juft = open("juft.txt", "a")
toq = open("toq.txt", "a")
for i in data:
    i = i.split(" ")
    for j in range(len(i)):
        if int(len(i[j])) % 2 == 0:
            juft.write(i[j] + ' ')
        else:
            toq.write(i[j] + ' ')

juft.close()
toq.close()
