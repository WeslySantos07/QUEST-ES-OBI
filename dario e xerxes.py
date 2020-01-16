n = int(input())
dx = [0]*2

for i in range(n):
    rec = list(map(int,input().split(" ")))    
    if rec[0] > rec[1]:
        if rec[0] - rec[1] > 2:
            dx[0] = dx[0] + 1
        else:
            dx[1] = dx[1] + 1
    else:
        if rec[1] - rec[0] > 2:
            dx[1] = dx[1] + 1
        else:
            dx[0] = dx[0] + 1
if dx[0] > dx[1]:
    print("dario")
else:
    print("xerxes")
