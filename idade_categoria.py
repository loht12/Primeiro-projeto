idade_atleta = int(input("Digite a idade do atleta:"))

if idade_atleta <= 9 :
    print ("Mirim.")
elif idade_atleta <= 14 :
    print ("Infantil.")
elif idade_atleta <= 19 :
    print ("Junior.")
elif idade_atleta <= 25 :
    print ("Sênior")
else:
    print("Master.")
