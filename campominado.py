from random import randint
m = [['*']*8,['*']*8,['*']*8,['*']*8,['*']*8,['*']*8,['*']*8,['*']*8]
n = [['*']*8,['*']*8,['*']*8,['*']*8,['*']*8,['*']*8,['*']*8,['*']*8]
p = 0
e = 0
c = 0
l = 0
g = 0

for i in range(8):
    for j in range(8):
        n[i][j] = randint(0,1)
        if n[i][j] == 0:
            g += 1

while p < g:
    print('=====================================')
    print('=============CAMPO==MINADO===========')
    print('=====================================')
    for i in range(8):
        for j in range(8):
            print(m[i][j],'  ', end=' ')
        print('\n')
    print('Digite a posicao!')
    c = int(input('DIGITE A COLUNA: '))
    l = int(input('DIGITE A LINHA: '))

    m[l][c] = n[l][c]
    
    if m[l][c] == 0:
        p += 1
    else:
        e += 1
        
    if e >= 3:
        break
    
print('====================================')
print('===============GAME==OVER===========')
print('SUA PONTUACAO FOI {}'.format(p - e))
    
    
