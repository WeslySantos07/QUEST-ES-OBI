n = int(input())
v = input()
v = list(map(int, v.split(' ')))
v.sort()

res = 'S'

if v[0] <= 8:
    for i in range(n-1):  
        if v[i+1]-v[i] > 8:
            res = 'N'
            break
else:
    res = 'N'

print (res)
