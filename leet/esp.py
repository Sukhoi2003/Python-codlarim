head = [1, 0, 1]

res=''
while head.next!=None:
    res+=str(head.val)
    head=head.next
res+=str(head.val)
res=res[::-1]
s=0
for i in range(len(res)):
    s+=int(res[i])*(2**i)
print(s)
