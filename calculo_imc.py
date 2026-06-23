# IMC
peso = float(input("Digite o peso kg :"))
altura = float(input("Digite sua altura m:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print ("Abaixo do preco")
elif imc >= 18.5 and imc <=24.9:
    print ("Peso ideal (Parabens!).")
elif imc >= 25.00 and imc <= 29.9:
    print ("Levemente acima do peso.")
elif imc >= 30.00 and imc <= 34.9:
    print ("Obesidade Grau 1.")
else:
    print ("Obesidade severa/morbida.")

