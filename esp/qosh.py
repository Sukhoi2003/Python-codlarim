l = open("salom.txt", "w")
def inp(en, uz):
    l.write(f"{en}: {uz}")


en = input("En ")
uz = input("Uz ")

inp(en, uz)
l.close()