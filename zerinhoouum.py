n = list(map(int, input().split()))

z = 0
u = 0

op = ["A","B","C"]

for i in range(3):
    if n[i] == 1:
        u = u + 1
    else:
        z = z + 1

if abs(u - z) != 3:
    if u<z:
        for i in range(3):
            if n[i]==1:
                res = i
                break
    else:
        for i in range(3):
            if n[i]==0:
                res = i
    print(op[res])
    
else:
    print("*")
