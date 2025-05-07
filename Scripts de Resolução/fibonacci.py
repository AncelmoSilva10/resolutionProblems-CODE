n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    prx = 0
    p = 0
    s = 1

    for i in range(2, n + 1):
        prx = p + s
        p = s
        s = prx

    print(prx)
