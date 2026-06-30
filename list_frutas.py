#print
lista_frutas = ["maca","melao","banana","goiaba","melancia","bergamota","laranja"]
print(lista_frutas[5])

#repeticao
for i in range(7):
    print(lista_frutas[i])

#escolha
escolha = int(input("Escolha uma fruta:"))
print (lista_frutas[escolha])

#repeticao
continuar = input("Quer continuar?")

while continuar == "s":
    print("maca","melao","banana","goiaba","melancia","bergamota","laranja")

