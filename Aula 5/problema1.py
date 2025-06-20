# Peça o primeiro nome e o sobrenome de uma pessoa. Inverta o conteúdo das variáveis. Imprima uma mensagem de boas vindas com as variáveis invertidas.

nome = input("Digite seu nome: ")

sobreNome = input("Digite seu sobrenome: ")

nome, sobreNome = sobreNome, nome

aux = nome
nome = sobreNome
sobreNome = aux


print(f"Seja bem vindo {nome} {sobreNome}")

