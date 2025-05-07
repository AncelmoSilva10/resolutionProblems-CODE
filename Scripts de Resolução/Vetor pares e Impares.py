vetor = []
vetorPar = []
vetorImpar = []


for i in range(10):
    valor = int(input())
    vetor.append(valor)

for i in range(10):
    if vetor[i] % 2 == 0:
        vetorPar.append(vetor[i])
    else:
        vetorImpar.append(vetor[i])

print(*vetorPar)
print(*vetorImpar)