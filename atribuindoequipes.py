v = list(map(int, input().split()))
v.sort()
e1 = v[0]+v[3]
e2 = v[1]+v[2]

res = [e1, e2]

print(max(res)-min(res))
