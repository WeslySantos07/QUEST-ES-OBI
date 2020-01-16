n,m = list(map(int, input().split()))
y = []
z = []
for j in range(n-1):
    x,c = list(map(int, input().split()))
    y.append(x)
    y.append(c)
a = list(set(y))
for j in range(m-1):
    x,c = list(map(int, input().split()))
    z.append(x)
    z.append(c)
b = list(set(z))
res_v = sum(a)-sum(b)
res_v = abs(res_v)
if res_v % 2 == 0:
    v = res_v//2
    print(v,v)
elif res_v % 2 != 0:
    t = res_v//2
    res_t = res_v - t
print(res_t,t)
    
