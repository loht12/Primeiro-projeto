valor_original= float(input("Digite o valor total:"))

if valor_original <= 100.00 :

    print ("Sem desconto.")

elif valor_original <= 300:
    desconto = valor_original * 0.05
    print("Voce conseguiu 5% de desconto!")
elif valor_original <= 500:
    desconto = valor_original * 0.1
    print("Voce conseguiu 10% de desconto")
else:
    print("Voce conseguiu 15% de desconto")

valor_total = valor_original - desconto
print(f"Valor original da compra sem desconto é:${valor_original: .2f}")
print(f"Valor do seu desconto foi:${desconto : .2f}")
print(f"Valor total a pagar com desconto:${valor_total: .2f} ")


valor_original= float(input("Digite o valor total:"))

if valor_original <= 100 :
    print(f"Sua compra foi de R$ {valor_original} e voce nao teve desconto")
elif valor_original <= 300 :
    desconto = valor_original * 0.05
    valor_original = valor_total- desconto
    print (f"Sua compra foi de R$ {valor_total} pois voce teve um desconto de R${desconto} e o seu pagamento final sera de R${valor_total}")
elif valor_original <= 500 :
    desconto = valor_original * 0.10
    valor_original = valor_total- desconto
    print (f"Sua compra foi de R$ {valor_total} pois voce teve um desconto de R${desconto} e o seu pagamento final sera de R${valor_total}")
else:
  desconto = valor_original* 0.15
  valor_total = valor_original - desconto
  print (f"Sua compra foi de R$ {valor_original} pois voce teve desconto de R${desconto} e o seu pagamento final sera de R${valor_total}")




