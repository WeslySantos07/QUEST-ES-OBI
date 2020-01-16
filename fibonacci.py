n = int(input())
v = [0]*(n+2)
v[0] = 0
v[1] = 1
cont = 2
res = 1
res2 = 0
while cont < n:
    var = res
    res = res + res2
    v[cont] = res
    cont = cont + 1
    res2 = var
for i in range(n):
    print(v[i], end=' ')
