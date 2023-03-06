i = 1
a=0
while i < 100:
    count = 0
 
    k = 2
    while i//2 >= k:
        if not i % k:
            count += 1
        k+=1
    if not count:
        m = 0
        l = 2
        a=i%10*10+i//10
        while a//2 >= l:
            if not a % l:
                m += 1
            l+=1
        if not m:
            print(i,end="<->")
            print(a)
    i+=1

