def almash(i:str):
    if i.find('left')>0:
        i=i[0:i.find('left')]+'right'+i[i.find('left')+4::]
        print(i,end=',')
    else:
        print(i,end=',')
    

a=list()
a.append(input("so'zlarni kiriting: "))
for i in a:
    i=i.split(" ")
    for j in i:
        almash(j)