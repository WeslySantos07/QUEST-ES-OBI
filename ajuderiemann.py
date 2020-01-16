n = int(input())
cont = [0]*2

i = 1
j = 1
p = 0

while cont[1] < n:
    if j % i != 0:
        cont[0] += 1

    if cont[0] == j-2:
        cont[0] = 0
        p = j
        cont[1]+=1
        j += 1
        i = 0
        
    if i == j:
        j+=1
        i = 0
        cont[0] = 0
        
    i += 1
    
print(p)
