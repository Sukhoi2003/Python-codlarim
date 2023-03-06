import requests

for i in range(100):
    print(i)
    requests.get("https://impossible-tictactoe.netlify.app/" + str(i))