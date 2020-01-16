t = [0]*6
for i in range(6):
    t[i] = int(input())
    
d = t[0] - t[3]
h = t[1] - t[4]
m = t[2] - t[5]

res = ((d*24)*60)*60
res += (h*60)*60
res += m*60

print(abs(res))
