#Crie um programa que pede a idade da pessoa e categoriza essa pessoa entre jovem, adulto e idoso.

idade = int(input("Digite sua idade: "))

if idade >= 60:
    print("Você é idoso.")
elif idade >= 0 and idade < 20:
    print("Você é jovem")
elif idade >= 20 and idade < 60:
    print("Você é adulto")
else:
    print("Você é anieligena")