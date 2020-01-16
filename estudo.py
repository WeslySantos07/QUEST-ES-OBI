n = int(input())
x = [int(i) for i in input().split()]
ultp = len(x)-1

cont5 = 0
ind = -1
for j in range(ultp):
    if(x[j] % 5 == 0):2
        cont5 += 1
        ind = j
        if(x[j] < x[ultp]):
            a = x[j]
            x[j] = x[ultp]
            x[ultp] = a

if(not x[ultp] % 5 == 0 and cont5 > 0):
   a = x[ind]
   x[ind] = x[ultp]
   x[ultp] = a 
if(cont5 == 0):
    print(-1)
else:
    for t in range(len(x)):
        if t == ultp:
            print(x[t])
        else:
            print(x[t], end=' ')
