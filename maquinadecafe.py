v = [int(input()), int(input()), int(input())]
m1 = 0
m2 = 0

pg = v.index(max(v))

if pg == 2:
    if v[2] < (v[0] + v[1]):
        pg = 1
elif pg == 0:
    if v[0] < (v[2] + v[1]):
        pg = 1

if pg == 0:
    m1 = v[1]*2
    m2 = v[2]*4
elif pg == 1:
    m1 = v[0] * 2
    m2 = v[2] * 2
else:
    m1 = v[0] * 4
    m2 = v[1] * 2

print(m1+m2)