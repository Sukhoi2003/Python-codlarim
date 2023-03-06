def list_word():
    with open("lugat.txt", "r") as f:
        data = f.read()
        print(data)
