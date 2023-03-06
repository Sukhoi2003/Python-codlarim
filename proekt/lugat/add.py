def inp():
    dic=dict()
    while True:
        l = open("lugat.txt", "a")
        a=open('lugat.txt','r')
        a=a.read()
        en = input("En ").capitalize()
        uz = input("Uz ").capitalize()
        a=a.split("\n")[:-1]
        for i in a:
            i=i.split(': ')
            dic[i[0]]=i[1]
        if en in dic:
            print("<<<This word exists🤷🏻>>>")
        else:
            l.write(f"{en}: {uz}\n")
        
        a=int(input("Do you add new word\n\t1.Yes\n\t0.No\n"))
        
        if a==1:
            continue
        else:
            l.close()
            break
