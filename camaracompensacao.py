v = input()
mn = list(map(int, v.split(" ")))

p = [0]*mn[1]
res = 0
valid = 0

x = [0]*mn[0]
v = [0]*mn[0]
y = [0]*mn[0]

for i in range (mn[0]):
    rec = input()
    rec = list(map(int, rec.split(" ")))
    x[i] = rec[0]
    v[i] = rec[1]
    y[i] = rec[2]
    p[x[i]-1] = p[x[i]-1] - v[i]
    p[y[i]-1] = p[y[i]-1] + v[i]
    valid = valid + v[i]

for i in range(mn[1]):
    res = res + abs(p[i])


if valid == res/2:
    print("N")
    print(int(res/2))
else:
    print("S")
    print(int(res/2))
