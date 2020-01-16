v = [0]*4
for i in range(4):
    v[i] = int(input())

r1 = (v[0]*60)+v[1]
r2  = (v[2]*60)+v[3]

if r1 + 45 <= r2:
    print('Sucesso')
else:
    print('Atrasado {}'.format((r1+45) - r2))
