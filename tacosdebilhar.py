n = int(input())
c = list(map(int, input().split()))
c.sort()

res = n * 2
ct = 0

for i in range(n-1):
    if c[i] == c[i+1] and ct != c[i]:
        res -= 2
        ct = c[i]
    elif c[i] == c[i+1]:
        ct = 0

print(res)
