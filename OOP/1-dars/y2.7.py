class myStr:

    def __init__(self) -> None:
        self.text = ""

    def setString(self, newStr):
        self.text = newStr

    def updateString(self):
        self.text = self.text[0].upper() + self.text[1:-1] + self.text[-1].upper()

n = input(">>> ")
m1 = myStr()
m1.setString(n)
m1.updateString()
print(m1.text)