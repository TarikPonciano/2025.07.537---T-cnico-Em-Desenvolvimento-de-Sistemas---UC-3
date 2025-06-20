cargo = input("Digite seu cargo: ")
salario = float(input("Digite seu salário: "))

#Expanda o programa para incluir a verificação de 3 cargos diferentes.  Para cada cargo, imprima uma mensagem customizada, além disso, calcule e exiba um valor de bônus diferente para cada um. Exemplo: Vendedor deverá ter um bônus de 15%, Analista deverá ter um bônus de 10%, etc

if cargo == "Vendedor":
    bonus = salario * 0.15
    print(f"Seja bem vindo, seu cargo é de Vendedor! Seu bônus é: R$ {bonus:.2f}")

if cargo == "Analista":
    bonus = salario * 0.10
    print(f"Seja bem vindo, seu cargo é de Analista! Seu bônus é: R$ {bonus:.2f}")

if cargo == "Gerente":
    bonus = salario * 0.05
    print(f"Seja bem vindo, seu cargo é de Gerente! Seu bônus é: R$ {bonus:.2f}")


