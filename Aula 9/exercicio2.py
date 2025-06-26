# Dos números de 0 a 200, conte quantos números são pares.

# numero = 2

# if (numero % 2 == 0):
#     print("É par!")
# else:
#     print("É impar!")
contador = 0

for i in range(201):
    print(i)
    if(i%2 == 0):
        contador += 1

print("Total de pares:", contador)