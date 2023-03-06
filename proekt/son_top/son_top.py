import random


def sontop(x=10):
    tasodifiy_son = random.randint(1,10)
    print(f"Assalomu alaykum.\nMen 1 dan 10 gacha son o'yladim topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin < tasodifiy_son:
            print("Xato. Men o'ylagan son kattaroq")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o'ylagan son kichikroq")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz")
    return taxminlar
#sontop()
def sontop_pc(x=10):
    input(f"1 dan 10 gacha son o'ylang va bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)\n>>> ".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"\\+++Topdim+++//.\n {taxminlar} ta taxmin blan topdim")
    return taxminlar


#sontop_pc()


def play(x=10):
    yana =1
    print(yana)
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("|++|++|++|-Men yutdim-|++|++|++|")
        elif taxminlar_pc > taxminlar_user:
            print("|++|++|++|-Siz yutdingiz-|++|++|++|")
        else:
            print("**Durrang roziman!**")
        yana = int(input("Yana o'ynamoqchimisz? Ha(1)/Yo'q(0):"))
        if yana==0:
            print("Xayr")
            return 0





def main():
    a=play()
    if a==0:
        return 0
    sontop()
    sontop_pc()



main()
