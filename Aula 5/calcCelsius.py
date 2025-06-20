c: int
f: int

f = float(input("Digite a temperatura em Fahrenheit: "))
c = (f - 32) * (5/9)

print(f"A temperatura de {f}°F é igual a {c:.2f}°C!")

if (c >= 20 and c < 40):
    print("Ta de boa!")
elif (c >= 40):
    print("Ta quente demais!")
else:
    print("Ta frio!")