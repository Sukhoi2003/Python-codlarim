try:
    with open("cinema.txt", "r") as f:
        film = f.read()
except FileNotFoundError:
    print("Fayl topilmadi")
else:
    film = film.split("\n")[:-1]

    for linya in film:
        linya = linya.split(",")
        if 2000 > int(linya[3]) and linya[2] == "Drama" or linya[2] == "Romance" or linya[2] == "Comedy":
            print(linya)