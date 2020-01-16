n = int(input())
m = []

for i in range(n):
    l = list(map(int, input().split()))
    m.append(l)

for i in range(1, n):
    for j in range(1, n):
        s = m[i][j-1] +  m[i-1][j-1] + m[i-1][j]
        if s > 1:
            m[i][j] = 0
        else:
            m[i][j] = 1
print(m[n-1][n-1])
