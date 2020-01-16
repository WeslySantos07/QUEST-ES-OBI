l1 = int(input())
l2 = int(input())
c1 = int(input())
c2 = int(input())
if l1 == l2:
    x = (l1+l2)*2
elif min(l1,l2)+1 == max(l1,l2):
    x = (l1+l2)*3
else:
    x = l1+l2
if c1 == c2:
    y = (c1+c2)*2
elif min(c1,c2)+1 == max(c1,c2):
    y = (c1+c2)*3
else:
    y = c1+c2
if x > y:
    print('Lia')
elif y > x:
    print('Carolina')
else:
    print('empate')
