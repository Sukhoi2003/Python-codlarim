def Calculator():
    while True:
        try:
        formula = input("Formula: ")
        lst = formula.split()
        if len(lst) != 3:
            raise ValueError
        a = float(lst[0])
        b = float(lst[0])
        if lst[1] not in "-+":
            raise ValueError
        if lst[1] == "+":
            print(a + b)
        else:
            print(a - b)
    except ValueError:
        print("Iltimos malumotni to'g'ri kiriting!!!")
    except Exception:
            print("")

Calculator()
