with open("fayl.txt", "r") as f:
    data = f.read()
data = data.split("\n")[:-1]
a = open("a.txt", "w")
k = open("k.txt", "w")
for i in data:
    if "A" in i:
        a.write(i)
    elif "a" in i:
        a.write(i)
    if "K" in i:
        k.write(i)
    elif "k" in i:
        k.write(i)    
a.close()
k.close()
