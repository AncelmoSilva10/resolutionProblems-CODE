
n = int(input())

lista = list(map(int, input().split()))

lista.sort()

for i in range(n):
    print(lista[i], end=" ")


