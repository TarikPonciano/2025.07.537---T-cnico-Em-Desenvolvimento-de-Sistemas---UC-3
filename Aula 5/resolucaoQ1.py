#Crie um programa que contém uma variável nome e as variáveis nota1, nota2, nota3 e nota4 que armazenam as informações de um aluno. Calcule a média desse aluno e exiba seu boletim e média.
#Exemplo:

'''
----- Boletim -----

Nome: João

Nota 1: 8.0
Nota 2: 7.0
Nota 3: 9.0
Nota 4: 6.0

Média: 7.5
'''
nomeAluno = input("Digite seu nome: \n")

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))
nota4 = float(input("Digite a nota 4:"))

somaNotas = nota1 + nota2 + nota3 + nota4

media = somaNotas / 4

print(f'''
----- BOLETIM ESCOLAR -----
      
Nome: {nomeAluno}

Nota 1: {nota1:.1f}
Nota 2: {nota2:.1f}
Nota 3: {nota3:.1f}
Nota 4: {nota4:.1f}

Média: {media:.1f}
''')