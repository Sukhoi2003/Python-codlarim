user = dict()
user["login"] = "sukhoi",
user["password"] = "12345678"

login = (input('login==> '))
password = (input('password==> '))

if user.get("login") == login and user.get("password") == password:
    print(user)
print(user)
