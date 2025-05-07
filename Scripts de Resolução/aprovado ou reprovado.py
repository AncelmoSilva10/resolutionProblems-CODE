n1 = float(input())
n2 =  float(input())

nota1 = n1 * 2
nota2 = n2 * 3

media = (nota1 + nota2)/5

if(media >= 7):
    print("Aprovado")
elif(media < 3):
    print("Reprovado")
else:
    print("Final")