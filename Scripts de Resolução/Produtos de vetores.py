vetor = list(map(int, input().split()))

vetores = [vetor[:2], vetor[2:]]

def produtoVetorial(ve):
    a, b = ve[0]
    c, d = ve[1]
    return (a * d) - (b * c)

pa = produtoVetorial(vetores)

def produtoEscalar(v):
    a, b = v[0]
    c, d = v[1]
    return (a * c) + (b * d)


pe = produtoEscalar(vetores)

print(pe, end=' ')
print(pa, end=' ')

