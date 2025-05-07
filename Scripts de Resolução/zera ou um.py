n1, n2, n3 = map(int, input().split())

if(n1 == n2 and n1 == n3):
    print("*")
elif(n1 != n2 and n2 == n3):
        print("A")
elif(n2 != n1 and n1 == n3):
        print("B")
elif(n3 != n1 and n2 == n1):
        print("C")



