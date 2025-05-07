n = int(input())

lista = list(map(int,input().split()))
vezes = 0

for i in range(n-2):
    if lista[i] == 1 and lista[i + 1] == 0 and lista[i + 2] == 0:
        vezes += 1

print(vezes)