n = int(input())
cont = 5
p = [0]*(n+4)
p[0] = 2
p[1] = 3
p[2] = 5
p[3] = 7
p[4] = 11
i = 2
while cont < n:

    if i%2 == 1 and i%3!=0 and i%n!=0 and i%7!=0 and i%9!=0 and i%11!=0:
        p[cont] = i
        cont = cont + 1
    i=i+1
        
print(p)
