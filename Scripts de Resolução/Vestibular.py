n = int(input())

lista1 = list(input())
lista2 = list(input())


acerto = 0

for i in range(0,n):
    if(lista1[i] == lista2[i]):
        acerto = acerto + 1

print(acerto)

