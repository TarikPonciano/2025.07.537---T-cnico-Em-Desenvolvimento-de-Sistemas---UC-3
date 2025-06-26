# frutas = ["Banana", "Maçã", "Abacate"]
# frutas[1] = "Jabuticaba"

# for fruta in frutas:
#     print(f"Hello {fruta}")


# nome = "Valdisnei"
# vogais = 0

# for letra in nome:
#     if (letra.lower() in "aeiou"):
#         vogais += 1

# print(f"Total de vogais em {nome}:", vogais)

for i in range(5):
    print("Hello")


# Peça o nome do usuário e imprima na tela 4x "Olá, {nome}"

nome = input("Digite o seu nome:")
repeticoes = int(input("Quantas vezes deseja repetir seu nome?"))

for i in range(repeticoes):
    print(f"{i+1} - Olá, {nome}!")



