text = "w3resouwrce"
count_let = dict()
for i in text:
    if i in count_let.keys():
        count_let[i] = count_let[i] + 1
    else:
        count_let[i] = 1
print(count_let)