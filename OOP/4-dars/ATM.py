from datetime import datetime

class Karta:
    def __init__(self, nomi, seriya, muddati, parol, summa):
        self.nomi = nomi
        self.seriya = seriya
        self.muddati = muddati
        self.parol = parol
        self.summas = summa

    def __str__(self):
        return f"""
        Kata Info
    Nomi : {self.nomi}
    Seriyasi : {self.seriya}
    Muddati : {self.muddati}
    Paroli : {self.parol}
    Summasi : {self.summas}
    """

    def getParol(self):
        return self.parol

    def setParol(self,currentParol, newParol):
        if self.parol == currentParol:
            self.parol = newParol
            return f"parol o'zgardi"
        else:
            return f"Eski parol xato"

    def getSumma(self):
        return self.summas

    def setSummaQosh(self, qosh):
        self.summas += qosh

    def setSummaOl(self, ol):
        self.summas -= ol


class User:
    def __init__(self, ism, familya, kata, naqtpul):
        self.ism = ism
        self.faml = familya
        self.karta = kata
        self.naqtpul = naqtpul

    def __str__(self):
        return f"""
        User Info
    Ismi : {self.ism}
    Familyasi : {self.faml}
    Karta : {self.karta}
    Naqd Puli : {self.naqtpul}
    """



class ATM:
    cach_money = 4000000
    def __init__(self, name, user: User):
        self.name = name
        self.user = user

    def getAtm(self):
        return f"""
        ATM Info
    Bank : {self.name}
    I.F : {self.user.ism} {self.user.faml}
    Karta seriya : {self.user.karta.seriya[:4]}{"*" * 8}{self.user.karta.seriya[-4:]} 
    """
    def pul(self,money):
        if self.user.karta.summas>=money and self.cach_money>money:
            self.user.karta.setSummaOl(money)
            self.cach_money-=money
            self.user.naqtpul+=money
            print("Amalyot muvafaqiyatli yakunlandi")
        else:
            print("Kartada mablag' yetarlimas")



class Menu:
    def menu(self):
        print("""
            Menu
    1.Kartadagi hisobni tekshirish
    2.Kartadan pul yechish
    3.kartaga pul solish
    4.Parolni ko'rish
    5.parolni o'zgartirish
        """)

# k.setSummaQosh(2000)
# k.setSummaOl(100)



k = Karta("QQB", "1234567891234567", "12/21", 2003, 100000)
user = User("Muhammadkarim", "Yo'ldashaliyev", k, 90000)
m = Menu()
print(m.menu())
# print(user)
atm = ATM("QQB", user)
#print(atm.getAtm())
#print(atm.cach_money)


n = int(input(">>> "))
if n == 1:
    print(user.karta.summas)
elif n == 2:
    atm.pul(int(input("Qancha pul yechmoqchisiz >>> ")))
    print(f"""
           +Chek+
    |+|-Sanasi -> {datetime.now()}                                   
    |+|-Ism    {user.ism}                                             
    |+|-Familya   {user.faml}                                         
    |+|-Bank kartasi {k.nomi}                                         
    |+|-Karta {user.karta.seriya[:4]}{"*" * 8}{user.karta.seriya[-4:]}
    |+|-Bankamad {atm.name}
    |+|-Kartadagi summa {atm.user.karta.summas}
    """)
elif n == 3:
    k.setSummaQosh(int(input("Qancha pul solmoqchisiz >>> ")))

elif n == 4:
    print(f"Kartangiz paroli ++|{k.getParol()}|++")
    print("""ESLATMA: Hech qachon hech kimga o'zingizning kartangiz ma'lumotlarini
    (karta chiqarilgan sana) va ayniqsa CVV (kartaning orqa qismidagi raqamlar) haqida
  aytmang. Pul o'tkazish uchun faqat karta raqamini bilish kifoya!""")
elif n == 5:
    print(k.setParol(int(input("Eski parolni kiriting>>> ")),int(input("Yangi parolni kiritng>>> "))))




# print(atm.cach_money)
# print(atm.user.naqtpul)

