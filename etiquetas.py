nkc = list(map(int, input().split(" ")))
arrN = list(map(int, input().split(" ")))
arrM = []
matriz = []
cont = 0
for i in range(nkc[0]-(nkc[2]-1)):
    arr = []
    for j in range(nkc[2]):
        arr.append(arrN[i+cont])
        cont += 1
    cont = 0
    matriz.append(arr)
    matriz[i] = sum(matriz[i])
for i in range(nkc[1]):
    menor = min(matriz)  
    pos = matriz.index(menor)
    num = pos - (nkc[2]-1)
    arrM.append(matriz[pos])
    matriz[pos] = 10001
    
    for j in range(nkc[2]-1):
        if num >= 0:
            matriz[num] = 10001
        num += 1
    num = pos + (nkc[2]-1)
    for j in range(nkc[2]-1):
        if num <= len(matriz):
            matriz[num] = 10001
        num -= 1
print(sum(arrN) - sum(arrM))
