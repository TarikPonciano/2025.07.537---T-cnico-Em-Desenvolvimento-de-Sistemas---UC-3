#Crie um programa que contém as variáveis nome, idade, altura e peso e imprima as informações no terminal.

'''
Nome: {nome}
Idade: {idade} anos
Altura: {altura} metros
Peso: {peso} kg
'''


nome = "Tarik"
idade = 29
altura = 1.7
peso = 70

# print("Nome: "+nome)
# print("Nome:",nome)
print(f"Nome: {nome}")

# print("Idade: "+idade+" anos")
# print("Idade:",idade,"anos")
print(f"Idade: {idade} anos")

print(f"Altura: {altura} metros")

print(f"Peso: {peso} kg")

print(f"""
Nome: {nome}
Idade: {idade} anos
Altura: {altura} metros
Peso: {peso} kg
""")

