import time

while True:
    opcao = int(input("""
    MENU
        1-Somar
        2- Subtrair
        3- Multriplicar
        4- Dividir
        5 - Sair
        Digite sua opcao:
    """))

    if opcao == 1 :
        print ("Soma")
    elif opcao == 2:
        print("Subtrair")
    elif opcao == 3:
        print("Multiplicacao")
    elif opcao == 4:
        print("Dividir ")
    elif opcao == 5:
        print("saindo...")
        time.sleep(1)
        break
    else:
        print("Opcão invslida, escolha uma nova")