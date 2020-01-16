vt = list(map(int, input().split()))
ct = 0
if vt[0] == vt[2] and vt[1] == vt[3]:
    ct = 0
else:
    if vt[0] != vt[1] and vt[2] != vt[3]:  
        ct = 1
    else:
        if vt[0] == 0:
            vt[0] = 1
        else:
            vt[0] = 0
        ct = 1
        if vt[0] != vt[2] and vt[1] != vt[3]:
            ct = 2
print(ct)
