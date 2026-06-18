salario_bruto = float(input("Digite salário bruto:"))
parcela = float(input("Digite o valor da parcela:"))
limite = salario_bruto * 0.3

if parcela <= limite :
    print ("Limite aprovado!")
else:
    print ("Limite não aprovado!")

