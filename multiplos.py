n = int(input())
vetor = [0]*n
cont2 = 0
cont3 = 0
cont4 = 0

for i in range (n):
    vetor[i] = int(input())
    for j in range (vetor[i]):
        if 2 * j == vetor[i]:
            cont2 = cont2 + 1
        if 3 * j == vetor[i]:
            cont3 = cont3 + 1
        if 4 * j == vetor[i]:
            cont4 = cont4 + 1
            
print(cont2)
print(cont3)
print(cont4)
