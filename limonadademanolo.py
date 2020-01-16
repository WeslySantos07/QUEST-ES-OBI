nc= list(map(int, input().split()))
res = 0
i  = nc[0]
j = nc[1]
while i > 0:
    res += nc[1]
    i -= 1
    if nc[1] > 1:
        nc[1] -= 1
print(res)
