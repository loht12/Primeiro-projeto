from traceback import print_tb

comprimento_A = float(input("Digite o comprimento l1 :"))
comprimento_B = float(input("Digite o comprimento l2:"))
comprimento_C = float(input("Digite o comprimento l2:"))

if comprimento_A + comprimento_B < comprimento_C or comprimento_A + comprimento_C <comprimento_B or comprimento_B + comprimento_C < comprimento_A :
    print ("Triangulo inválido")
else:
    print ("Triangulo valido")
    if comprimento_A == comprimento_B == comprimento_C:
        print ("Todos os lados iguais,Equilátero:")
    elif comprimento_A == comprimento_B or comprimento_A==comprimento_C or comprimento_B == comprimento_C:
        print ("Dois lados iguais,Isósceles:")
    else:
        print ("Todos os lados diferentes,Escaleno:")
