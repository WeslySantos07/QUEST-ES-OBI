c = int(input())
v = [0]*7
v[1] = c//100
res = c%100
v[2] = res//50
res = res%50
v[3] = res//25
res = res%25
v[4] = res//10
res = res%10
v[5] = res//5
res = res%5
v[6] = res

v[0] = sum(v)

for i in range(7):
    print(v[i])
