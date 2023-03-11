s = "the sky is blue"
s = s.split(" ")
print(s)
c = ""

for i in range(len(s)-1):
    c+=s[len(s)-i-1]
    c+=" "
c+=s[0]

print(c)