# Lista de times de A a P
times = list("ABCDEFGHIJKLMNOP")

# Leitura dos 15 resultados
placares = [tuple(map(int, input().split())) for _ in range(15)]

idx = 0  # índice dos placares

# Enquanto houver mais de 1 time, continua a competição
while len(times) > 1:
    proxima_fase = []
    for i in range(0, len(times), 2):
        time1 = times[i]
        time2 = times[i + 1]
        gols1, gols2 = placares[idx]
        idx += 1

        if gols1 > gols2:
            proxima_fase.append(time1)
        else:
            proxima_fase.append(time2)

    times = proxima_fase  # atualiza a lista com os classificados

# Exibe o campeão
print(times[0])
