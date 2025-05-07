N, D, M, P = map(int, input().split())


danoAnterior = N * D
danoAtual = M * P

if danoAtual > danoAnterior:
    print("BUFF")
else:
    print("NERF")
