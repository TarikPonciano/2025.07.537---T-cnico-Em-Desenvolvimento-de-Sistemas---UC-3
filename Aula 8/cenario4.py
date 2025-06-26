#Cenário 4 - Crie um programa que valida se um nome é válido. Para ser válido o nome deve ter pelo menos 5 caractéres e começar com uma vogal. Exiba na tela uma mensagem de erro caso o nome não seja válido. (Para resolver essa situação será necessário conhecer o operador 'in')

nome = input("Digite um nome válido: ")

# Força Bruta
# if (len(nome) >= 5) and (nome[0] == "a" or nome[0] == "e" or nome[0] == "i" or nome[0] == "o" or nome[0] == "u"):
#     print("O nome é válido!")
# else:
#     print("O nome é inválido!")

if (len(nome) >= 5) and (nome[0].lower() in "aeiou"):
    print("O nome é válido!")
else:
    print("O nome é inválido!")