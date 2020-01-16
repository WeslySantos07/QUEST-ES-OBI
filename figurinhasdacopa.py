n,c,m = list(map(int, input().split()))
xc = [0]*c
xm = [0]*m
cont = 0
xc = list(map(int, input().split()))
xm = list(map(int, input().split()))
for i in range(c):
    for j in range(m):
        if xc[i] == xm[j]:
            cont = cont + 1
print(c-cont)
