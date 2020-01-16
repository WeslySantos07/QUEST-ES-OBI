n = int(input("digite o número de botas: "))
m = [0]*n
l = [0]*n
for i in range(n):
    m[i] = int(input("digite o tamanho da bota: "))
    l[i] = input("digite o lado da bota: ")
pf = 0
for i in range(n):
    for j in range (n):
        if m[i] == m[j] and l[i] != l[j]:
            pf = pf + 1
            

print (pf)
            
