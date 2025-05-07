tamanho = int(input())
vetor = list(map(int, input().split()))
n = int(input())

tem = 0

for i in range(tamanho):
    if vetor[i] == n:
        tem += 1

if tem>=1:
    print('pertence')
else:
    print('nao_pertence')