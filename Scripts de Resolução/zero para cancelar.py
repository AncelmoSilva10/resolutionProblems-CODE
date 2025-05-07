n = int(input())
lista = []

for i in range (0,n):
    x = int(input())

    if x == 0 and lista:
        lista.pop()
    else:
        lista.append(x)

print(sum(lista))