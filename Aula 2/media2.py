qtd = int(input("Digite quantos números deseja calcular na média: "))

soma = 0

for i in range(qtd):
    n = int(input(f"Digite o número {i}: "))
    soma = soma + n

# Verificar se soma deu 0

media = soma/qtd
print(f"A média dos números é: {media}")
