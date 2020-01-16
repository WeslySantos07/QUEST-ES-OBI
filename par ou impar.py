p = int(input())
d=[0]*2
d[0]=int(input())
d[1]=int(input())

if (d[0] + d[1]) % 2 == 0:
    print(p)
else:
    if p == 0:
        print(1)
    else:
        print(0)
