n = int(input())
m = int(input())
vetor = [0]*m
cont = 0
for i in range(m):
    vetor[i] = int(input())
vetor.sort()
for i in range(m-1):
    if vetor[i] == vetor[i+1]:
         m -= 1
print(n - m)
