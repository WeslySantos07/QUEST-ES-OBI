matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0, 3):
     for l in range(0, 3):
          matriz[c][l] = int(input())
c1= matriz[0][0]+matriz[1][1]+matriz[2][2]
c2 = matriz[2][0]+matriz[1][1]+matriz[0][2]
print("Diagonal principal:",c1)
print("Diagonal secundaria:",c2)

