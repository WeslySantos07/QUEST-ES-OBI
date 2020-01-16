import math

n = int(input())
x= [0]*(n*2)
y= [0]*(n*2)
cont = 0
num = 0

for i in range (n):
    rec = input()
    rec = list(map(int, rec.split(" ")))
    x[cont] = rec[0]
    x[cont+1] = rec[2]
    y[cont] = rec[1]
    y[cont+1] = rec[3]
    cont = cont + 2

m = n*2

i = 0
j = 0

while i < m:
    while j < m:
        if (x[i] <= x[j] and y[i] >= y[j]) and (x[i+1] >= x[j+1] and y[i+1] <= y[j+1]):
            num = num + 1
        ##print(x[i],',',x[j],',',y[i],',',y[j])
        ##print(x[i],',',x[j+1],',',y[i+1],',',y[j+1])
        j = j + 2
    j = 0
    i = i + 2

num = num - n
##num = math.floor(num/2)
print(num)
