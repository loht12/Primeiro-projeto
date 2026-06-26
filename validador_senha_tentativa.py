senha_correta = 123456

for i in range (2,-1,-1):
    senha_digitada = int(input("Digite a sua senha:"))
    if senha_digitada == senha_correta:
        print("Acesso liberado.")
        break
    else:
        print(f"Senha incorreta, voce tem mais {i} tentativas")
else:
    print("Conta bloqueada.")
