# Dos números de 0 a 200, conte quantos números são pares.

# numero = 2

# if (numero % 2 == 0):
#     print("É par!")
# else:
#     print("É impar!")
contador = 0
numeros = ""

for i in range(201):
    # numeros += str(i) + " - " if i != 200 else str(i)
    if i == 200:
        numeros += str(i)
    else:
        numeros +=  str(i) + " - "
    if(i%2 == 0):
        contador += 1

print("Numeros:", numeros)

print("Total de pares:", contador)
