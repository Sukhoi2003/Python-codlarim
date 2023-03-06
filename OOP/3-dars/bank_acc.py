import uuid

class Bank:
    def __init__(self, ownername, ownerphonnumber):
        self.__hisob = 0.0
        self.__mijos = ownername
        self.__id = uuid.uuid4()
        self.__telefon = ownerphonnumber
        self.__tarix = dict()

    def getInfo(self):
        print(f"""
            Info
        Balans : {self.__hisob}
        Telefon : {self.__telefon}
        Tarixi : {self.__tarix}
        """)
    def getBalans(self):
        return self.__hisob

    def setBalans(self, newHisob):
        self.__hisob = newHisob

    def getMijoz(self):
        return self.__mijos

    def getId(self):
        return self.__id

    def setId(self, newId):
        self.__id = newId


    def getTel(self):
        return self.__telefon

    def setTel(self, newtel):
        self.__telefon = newtel

    def getHistry(self):
        return self.__tarix

    def setHistry(self, newHstr):
        """

        :rtype: object
        """
        self.__tarix = newHstr

a = uuid.uuid4()

c = Bank(input("Ism: "), int(input("Tel: ")))
c.setBalans(int(input('Balans: ')))
c.setHistry(input("Tarix: "))
c.setId(a)
c.setTel('998 93 130 70 15')
print(c.getInfo())
print("%%%%%%%%%%%%%%%%%%")
print(c.getBalans())
print("%%%%%%%%%%%%%%%%%%")
print(c.getId())
print("%%%%%%%%%%%%%%%%%%")
print(c.getMijoz())
print("%%%%%%%%%%%%%%%%%%")
print(c.getId())
print("%%%%%%%%%%%%%%%%%%")
print(c.getHistry())


