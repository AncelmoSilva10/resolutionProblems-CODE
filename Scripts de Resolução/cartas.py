a = int(input())
b = int(input())
c = int(input())

if a == b and b!=c:
    print(c)
elif a==c and c!=b:
    print(b)
elif b==c and c!=a:
    print(a)