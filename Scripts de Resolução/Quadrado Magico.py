n = int(input())


matriz = []


for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)


dp = sum(matriz[i][i] for i in range(n))


ds = sum(matriz[i][n-i-1] for i in range(n))


sl = [sum(matriz[i]) for i in range(n)]


sc = [sum(matriz[i][j] for i in range(n)) for j in range(n)]

print(dp, sl, ds, sc)

if dp == ds and dp == sl[0] and dp == sc[0]:
    print(dp)
else:
    print(-1)
