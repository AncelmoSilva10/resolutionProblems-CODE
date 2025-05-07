estado = input()

estados = ['para', 'rondonia', 'acre', 'amapa', 'roraima', 'tocantins']

for i in estados:
    if i == 'estado':  # Verifica diretamente o elemento
        print('Regiao Norte')
        break  # Para o loop imediatamente
    else:
        print('Outra regiao')
