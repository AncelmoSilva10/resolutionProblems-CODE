op = input()
n, n1 = map(float, input().split())

if op == 'M':
    print(f"{n * n1:.2f}")
elif op == 'D':
    print(f"{n / n1:.2f}")