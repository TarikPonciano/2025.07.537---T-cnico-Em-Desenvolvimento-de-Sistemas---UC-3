#Crie um programa que contém pelo menos 4 informações de um funcionário (criar variáveis) e imprima de maneira formatada abaixo. Exemplo:

"""
######### INFORMAÇÕES PESSOAIS #########

ID - {informacao1}
Nome - {informacao2}
Cargo - {informacao3}
Salário - R$ {informacao4}
"""

idFunc = 153
nome = "Marquinhos Johnson"
cargo = "Analista"
cpf = "02345678910"
salario = 5000.00

print(f'''
######### INFORMAÇÕES PESSOAIS #########

ID - {idFunc}
Nome - {nome}
Cargo - {cargo}
CPF - {cpf}
Salário - R$ {salario:.2f}
''')