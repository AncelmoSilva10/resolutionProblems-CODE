vetor = []
vezes = 0
ocorrencia = []

for i in range(10):
    valor = int(input())
    vetor.append(valor)

menor = min(vetor)


for i in range(10):
    if vetor[i] == menor:
        ocorrencia.append(i)
        vetor[i] = -1

print('Menor:',menor)
print('Ocorrencias:',*ocorrencia)
print(*vetor)