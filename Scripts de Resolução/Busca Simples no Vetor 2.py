vetor = list(map(int,input().split()))
n = int(input())

vezes = 0
posicao = []

for i in range (10):
    if n == vetor[i]:
        vezes += 1
        posicao.append(i)

if vezes >= 1:
    print(vezes)
    print(*posicao)
else:
    print('Mia x')
