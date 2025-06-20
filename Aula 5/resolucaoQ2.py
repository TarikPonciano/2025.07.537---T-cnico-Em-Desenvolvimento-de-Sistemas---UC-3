#Calcule e imprima a área de um retângulo 

#Faça as seguintes melhorias: 
#1. Peça para o usuário digitar as dimensões de retângulo
#2. Ao imprimir, exiba a mensagem "A área do retângulo é: {area} m²"

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
print(f"A área do retângulo é {area} m²!")