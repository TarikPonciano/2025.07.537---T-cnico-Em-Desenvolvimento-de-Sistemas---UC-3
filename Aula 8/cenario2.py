#Cenário 2 - Crie um programa que pede ao usuário 3 números inteiros. Exiba na tela os três números em ordem decrescente.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Estratégia 1
# if n1 >= n2 and n1 >= n3 and n2 >= n3:
#     print(f"A ordem é: {n1} > {n2} > {n3}")
# elif n1 >= n2 and n1 >= n3 and n3 >= n2:
#     print(f"A ordem é: {n1} > {n3} > {n2}")

# Estratégia 2
if n1 >= n2 and n1 >= n3:
    primeiro = n1

    if n2 >= n3:
        segundo = n2
        terceiro = n3
    else:
        segundo = n3
        terceiro = n2

elif n2 >= n1 and n2 >= n3:
    primeiro = n2

    if n1 >= n3:
        segundo = n1
        terceiro = n3
    else: 
        segundo = n3
        terceiro = n1
else:
    primeiro = n3

    if n1 >= n2:
        segundo = n1
        terceiro = n2
    else:
        segundo = n2
        terceiro = n1

print(f"A ordem decrescente dos números é: {primeiro} > {segundo} > {terceiro}")

# numeros = [n1,n2,n3]
# numeros.sort(reverse=True)
# print(f"A ordem decrescente dos números é: {numeros}")
