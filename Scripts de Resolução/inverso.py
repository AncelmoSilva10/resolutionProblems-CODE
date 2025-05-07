lista = []

for i in range(0, 10):
    n = int(input())
    lista.append(n)

for i in range(0,10):
    lista.sort(reverse=True)
    print(lista[i])