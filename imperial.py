n = int(input())
v = [0]*n
cont = 0
for i in range(n):
     v[i] = int(input())
for i in range(n):
     for j in range(i):
          if v[i] == v[j+1]:
               cont += 1
print(abs(cont-n))

