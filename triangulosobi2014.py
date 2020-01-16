v = list(map(int, input().split()))
v.sort()
res = False
for i in range(2):
    if v[i] < v[i+1] + v[i+2] and v[i+1] < v[i] + v[i+2] and v[i+2] < v[i+1] + v[i]:
        res = True

if res:
    print('S')
else:
    print('N')