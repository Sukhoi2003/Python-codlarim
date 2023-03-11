1---#########################################################
filename = "file.txt"

with open(filename) as f:
   for line in f:
       print(line)

with open(filename) as f:
   siyosat = f.readlines()

print(siyosat)

siyosat = [siyosat.rstrip() for siyosat in siyosat]
print(siyosat)
2---------#######################################################
ism = "Muhammadkarim Yo'ldashaliyev"
yil = 2003
with open("write.txt", "w") as f:
   f.write(ism)
   f.write(str(yil))
#########################################
ism = "Muhammadkarim Yo'ldashaliyev"
yil = 2003
with open("write.txt", "w") as f:
   f.write(ism+"\n")
   f.write(str(yil)+"\n")
k.v#########################################
with open("file.txt", "r") as f:
   data = f.read()

data = data.split("\n")[:-1]
for item in data:
   item = item.split()
   print(item)

with  open("yangi.txt", "r") as f:
   data = f.write("Aliyev Ali")

print(data)
