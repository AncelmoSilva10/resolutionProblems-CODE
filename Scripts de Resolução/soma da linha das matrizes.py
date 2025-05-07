matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

for i, linha in enumerate(matriz):
    print(f"Linha {i}: {sum(linha)}")
