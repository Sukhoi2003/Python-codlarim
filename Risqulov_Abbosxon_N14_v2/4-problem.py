with open('tovar.txt','r') as f1:
    f1=f1.read()
f1=f1.split()
print(f1)
a=open("Aharfli.txt",'w')
k=open("Kharfli.txt",'w')
for i in f1:
    if i[0]=='K' or i[0]=='k':
        k.write(i+' ')
    if i[0]=='A' or i[0]=='a':
        a.write(i+' ')
a.close()
k.close()


