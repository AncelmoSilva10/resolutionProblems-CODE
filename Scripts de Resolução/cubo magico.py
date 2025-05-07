n = int(input())
matriz = []
dp = 0
ds = 0

for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)


for i in range(n):
    dp += matriz[i][i]


for i in range(n):
    ds += matriz[i][n - 1 - i]


soma_certa = dp
valido = True


for linha in matriz:
    if sum(linha) != soma_certa:
        valido = False
        break

for j in range(n):
    soma_coluna = 0
    for i in range(n):
        soma_coluna += matriz[i][j]
    if soma_coluna != soma_certa:
        valido = False
        break

if dp != ds:
    valido = False

if valido:
    print(soma_certa)
else:
    print(-1)
