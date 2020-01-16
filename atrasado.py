ha = int(input())
ma = int(input())
hr = int(input())
mr = int(input())
ha = ha*60
hr = hr*60
x = (hr+mr) - (ha+ma+45)
if x < 0:
    print('Atrasado {}'.format(x*-1 ))
else:
    print('Sucesso')
