n = int(input())
xy1 = list(map(int, input().split(" ")))
xy2 = list(map(int, input().split(" ")))
y = x = False
if (xy1[0] > (n/2) and xy2[0] > (n/2)):
    x = True
    
if not x:
    if (xy1[0] <= (n/2) and xy2[0] <= (n/2)):
        x = True
        
if (xy1[1] <= (n/2) and xy2[1] <= (n/2)):
    y = True
    
if not y:
    if (xy1[1] > (n/2) and xy2[1] > (n/2)):
        y = True

if x == True and y == True:
    print("N")
else:
    print("S")
