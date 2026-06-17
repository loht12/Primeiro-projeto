# Casar ou Comprar uma Bicicleta  ?

print("Casar ou comprar uma bicicleta ?")

resposta = input("Voce esta gordo ? s/n:")

if resposta == "s":
  quer_emagrecer = input("Voce quer emagrecer ? s/n:")
  if quer_emagrecer == "s":
    print("compre uma bicicleta!")
  else:
    print("Entao case!")
else:
     quer_engordar = input("Voce quer engordar ? s/n:")
     if quer_engordar == "s":
         print("entao case!")
     else:
         print("compre uma bicicleta!")

