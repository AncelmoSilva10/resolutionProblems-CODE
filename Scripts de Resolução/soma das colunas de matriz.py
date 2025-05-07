matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    print(f'Coluna {j}:', soma)

