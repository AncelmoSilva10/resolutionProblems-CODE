n = int(input())
lista = list(map(int,input().split()))
q = int(input())
listaSairam = list(map(int,input().split()))

r = n - q

for item in listaSairam:
    if item in lista:
        lista.remove(item)

print(*lista)
