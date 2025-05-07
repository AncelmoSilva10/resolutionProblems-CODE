matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)


maior = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

for i in range(3):
    for j in range(3):
        if matriz[i][j] == maior:
            matriz[i][j] = -1


for linha in matriz:
    print(*linha)
