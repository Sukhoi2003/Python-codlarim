def slt(text):
    count = int()
    count1 = int()
    for i in text:
        if i.isupper():
            count += 1
        elif i.islower():
            count1 += 1
    return (count, count1)

print(list(slt(input('>>>> '))))
