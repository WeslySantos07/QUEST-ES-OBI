n = list(map(int, input().split(" ")))

cont = 0

for i in range(2):
    if n[i] == n[i+2]:
        cont = cont + 1

if cont > 0:
    print("V")
else:
    print("F")
