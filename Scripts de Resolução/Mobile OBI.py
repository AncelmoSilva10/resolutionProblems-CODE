a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b == c:
    if b + c == d:
        if a == b + c + d:
            print('S')
        else:
            print('N')
    else:
        print('N')
else:
    print('N')