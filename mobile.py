a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = 0

if a == b+c+d:
    x += 1
    if (b+c) == d:
        x += 1
        if b == c:
            x += 1
            
if x == 3:
    print('S')
else:
    print('N')
