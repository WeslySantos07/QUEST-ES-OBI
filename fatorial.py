n = int(input())
m = n - 1
res = n
i = n
if n == 0:
    print(1)
else:
    while i > 1:
        res = res * m
        m = m-1
        i = i-1
    print(res)
