n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a nota 2:"))
media = (n1 + n2)/2

if media >= 7:
    print ("Aprovado")
elif media >= 3 and media < 7:
    print("Recuperação")
else:
    print ("Reprovado")
