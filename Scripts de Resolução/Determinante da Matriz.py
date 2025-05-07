matriz = []
diagonalPrincipal = 0
diagonalSecundaria = 0

def determinante(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + h * f * a)

for i in range(3):
    linha = list(map(int, input().split()))
    matriz.append(linha)

det = determinante(matriz)
print(det)


