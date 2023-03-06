def search():
    with open("lugat.txt", "r") as f:
        data = f.readlines()
        en = input("Qidirayaotgan so'zingizni kiriting >>> ").capitalize()
        lst = list()
        ind = 0
        for i in data:
            if en in i:
                lst.insert(ind, i)
        if len(lst) == 0:
            print("So'z topilmadi")    
        else:
            for n in range(len(lst)):
                print(end=lst[n])
        print("davom etasizmi")

    


     
