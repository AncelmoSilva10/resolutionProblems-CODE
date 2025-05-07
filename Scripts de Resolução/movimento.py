x = float(input())
y = float(input())
z = float(input())

horarioMinimo = x + y
horarioDeterminado = z + 0.5

if horarioMinimo >= horarioDeterminado:
    print(0)
else:
    print(1)