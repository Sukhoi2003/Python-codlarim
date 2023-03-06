a=input('')
z={'01':'January','02':'febrary','03':'March','04':'April','05':'May','06':'June','07':'July','08':'august','09':'September','10':'October','11':'November','12':'December'}
b=list()
c=list()
b.append(a)
for i in b:
    i=i.split('.')
    for j in i:
        j=j.split(' ')
        for q in j:
            q=q.split(':')
            c.append(q)
print(c)
print(f"{c[0][0]} {z[c[1][0]]} {c[2][0]} year  {c[3][0]} hours {c[3][1]} minutes")