a = int(input())
b = int(input())
v1 = [1,2,0]*a
v = [1,2,0]
cont = 0
for i in range(a):
    cont += 1
v.remove(v1[i])
v2 = v*b
for j in range(b):
    cont += 1
v.remove(v2[j])
print(v[-1])
