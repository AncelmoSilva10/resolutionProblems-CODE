n = int(input())
vetor = list(map(int, input().split()))
media = sum(vetor) / len(vetor)
print(f'{media:.2f}')