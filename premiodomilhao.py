n = int(input())
v = [0]*n
for i in range(n):
    v[i] = int(input())

res = 0
i = 0

while res < 1000000:
    res += v[i]
    i += 1

print(i)
