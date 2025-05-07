matriz = []
diagonalPrincipal = 0
diagonalSecundaria = 0

for i in range(3):
    linha=[]
    for j in range(3):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)


for i in range(3):
    diagonalPrincipal += matriz[i][i]

for j in range(3):
    diagonalSecundaria += matriz[j][2 - j]

print ('Diagonal principal:',diagonalPrincipal)
print ('Diagonal secundaria:', diagonalSecundaria)