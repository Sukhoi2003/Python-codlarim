social = ["Instgram", "Facebook", "Telegram", "Tik-Tok", "Radiogram"]


str = list(filter(lambda i : 'gram' in i, social))

print(str)