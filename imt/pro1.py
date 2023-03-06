def myfunc(text: list):
    """List qabul qiladi
    :type text: object
    """
    for i in text:
        if i[0] == 'k' or i[0] == 'K':
            print(i)


text = list(map(str, input().split()))
myfunc(text)
