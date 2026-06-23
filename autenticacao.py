nome_de_usuario = (input("Nome do usuário:"))
chave_de_seguranca = int(input("Chave de seguranca:"))

if nome_de_usuario != "admin" or chave_de_seguranca != 9988:
    print ("Usuario ivalido e chave de seguranca invalido.")
else:
    print("Dados de acesso válidos.")