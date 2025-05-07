n = int(input())
lista = list(map(int, input().split()))

maximo = 1
atual = 1

for i in range(1, n):
    if lista[i] == lista[i-1]:
        atual += 1
        maximo = max(maximo, atual)
    else:
        atual = 1

print(maximo)

