n = int(input())
vt = list(map(int, input().split()))
a = 0
b = 0
c = 1
cont = 0
for i in range(n):
    if vt[i] == 1:
        x = a
        a = c
        c = x
    else:
        if a == 0:
            a = 1
            c = 0
        else:
            a = 0
            c = 1
        if b == 0:
            b = 1
        else:
            b = 0
        
print(a)
print(b)
