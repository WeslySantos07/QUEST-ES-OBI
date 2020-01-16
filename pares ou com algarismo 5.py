X = input()
Y = input()
Z = input()

vetor = [int(X),int(Y),int(Z)]
cont = 0

ultimo_caractere_x = X[-1::]
ultimo_caractere_y = Y[-1::]
ultimo_caractere_z = Z[-1::]


vetor_ultimos_caracteres = [ultimo_caractere_x,ultimo_caractere_y,ultimo_caractere_z]


for i in range(3):
    if vetor[i]%2 == 0:
        cont = cont + 1
    elif  vetor_ultimos_caracteres[i] == "5":
        cont = cont + 1
    
print(cont)
