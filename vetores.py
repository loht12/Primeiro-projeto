from turtledemo.penrose import start
from turtledemo.round_dance import stop

lista_frutas = ["maca","melao","banana","goiaba","melancia","bergamota","laranja","pera","abacate"]
print (lista_frutas[-1])
#QUANDO QUISER CONTAR DO ULTIMO AO PRIMEIRO USE "-"

#print("\n ALuno".join(lista_frutas)"

#deixa em ordem
lista_frutas.sort()
notas = [9.3,5.6,3.5,6.7,8.3]
print(lista_frutas[2])

#add mais um
lista_frutas.append("Manga")
#remove o ultimo
lista_frutas.pop()
#remove na posicao 2
lista_frutas.pop(2)
#remove
lista_frutas.remove("bergamota")
#apaga
lista_frutas.clear()
#procura em um intervalo
encontrou = lista_frutas.index(value:"maca", start:1, stop:6)
print (encontrou)
for i in range(len(lista_frutas)):
    print(f"{i+1} fruta {lista_frutas[i]}")

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

#O melhor

for frutas in lista_frutas:
    print(frutas)

contador = 0
while contador < len(lista_frutas):
    print(lista_frutas[contador])
    contador += 1

pessoa = ["Lorrany", 21, 1.60, True, "F"] # Vetor

