numeros = []

qtd = int(input("Digite quantos números deseja calcular: "))

for i in range(qtd):
    num = int(input("Digite um número: "))
    numeros.append(num)

media = sum(numeros)/len(numeros)

print(f"A média é: {media}")
print(f"Lista de números: {numeros}")