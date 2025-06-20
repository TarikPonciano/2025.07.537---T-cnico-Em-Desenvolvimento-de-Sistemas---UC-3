n1 = int(input("Digite o número 1: "))

n2 = int(input("Digite o número 2: "))

n3 = int(input("Digite o número 3: "))

if (n1 == 0) and (n2 == 0) and (n3 == 0):
    print("Os dois números são iguais a 0. Comece de novo...")
    exit()

resultado = (n1 + n2 + n3)/3

print("O resultado é:", resultado)



