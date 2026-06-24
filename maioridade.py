maiores_idade = 0
menores_idade = 0

for i in range (1, 8):

    ano_nascimento = int(input(f"Digite o ano de nascimento da {i} pessoa: "))

    idade = 2026 - ano_nascimento

    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f"\n Quantidade de maiores de idade: {maiores_idade} e a quantidade de menores de idade: {menores_idade}")