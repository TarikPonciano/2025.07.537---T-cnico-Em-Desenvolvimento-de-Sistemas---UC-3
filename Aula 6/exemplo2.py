#Crie um programa que pede o nome e 4 notas de um aluno. Calcule a média do aluno e exiba se esse aluno foi Aprovado, Reprovado ou está de Recuperação.

nome = input("Digite seu nome: ")

nota1 = float(input("Digite sua nota: "))

nota2 = float(input("Digite sua nota: "))

nota3 = float(input("Digite sua nota: "))

nota4 = float(input("Digite sua nota: "))

media = round(((nota1 + nota2 + nota3 + nota4) / 4), 1)

if ((media >= 7) and (media <= 10)):
    print(f"O aluno {nome} foi Aprovado com média {media}.")
elif media < 7 and media >= 4:
    print(f"O aluno {nome} está de Recuperação com média {media}.")
elif media >= 0 and media < 4:
    print(f"O aluno {nome} foi Reprovado com média {media}.")
else:
    print("Média inválida.")