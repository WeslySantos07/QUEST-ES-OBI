matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0, 3):
     for l in range(0, 3):
          matriz[l][c] = int(input())
c1= matriz[0][0]+matriz[1][0]+matriz[2][0]
c2 = matriz[0][1]+matriz[1][1]+matriz[2][1]
c3 = matriz[0][2]+matriz[1][2]+matriz[2][2]
print("Linha 0:",c1)
print("Linha 1:",c2)
print("Linha 2:",c3)

