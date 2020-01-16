n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
res = 0
c = 0

for i in range(n):
    res = x[i]
    if res == k:
            c += 1
    for j in range(i+1, n):
        res += x[j]
        
        if res == k:
            c += 1

print(c)
