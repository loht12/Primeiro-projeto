import random
from operator import truediv
from selectors import SelectSelector

num_digitado = int(input("Digite um número:"))

numero_gerado = random.randint (1,20)
print (f"Número secreto {numero_gerado}")

if num_digitado == numero_gerado :
    print("Parabéns voce acertou.")
elif num_digitado < numero_gerado :
    print ("Menor que o valor advinhado.")
else:
    print ("Numero maior que o valor digitado.")



