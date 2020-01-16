x = int(input())
y = int(input())

if x >0 and y > 0 :
    res = 'Q1'
elif x >0 and y< 0:
    res = 'Q4'
elif x <0 and y> 0:
    res = 'Q2'
elif x<0 and y <0:
    res = 'Q3'
else:
    res = 'eixos'

print(res)
