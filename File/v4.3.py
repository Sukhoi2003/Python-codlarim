try:
    with open("cinema.txt", "r") as f:
        film = f.read()
except FileNotFoundError:
    print("Fayl topilmadi")
else:
    film = film.split("\n")[:-1]

    for linya in film:
        linya = linya.split(",")
        if int(linya[-1][:-3]) > 17 and linya[2] == "Horror":
            print(*linya)