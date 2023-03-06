import math
from tkinter import *

oyna = Tk()

oyna.title("qoshish funksiyasi")
oyna.geometry("300x300")

natija = Label(text="Natija", bg="gray")
natija.place(x=70, y=45, width=145, height=30)


qosh = Entry()
qosh.place(x=70, y=90, width=140, height=25)


def salom():
    natija = math.factorial()

tugma = Button(text="Hisoblash", command=salom, bg="gray")
tugma.place(x=80, y=150, width=120, height=40)

oyna.mainloop()
