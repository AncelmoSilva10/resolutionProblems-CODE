import math

n = int(input())

valores = list(map(float, input().split()))


for num in valores:
    print(f"{math.sqrt(num):.4f}")


