# Cenário 2 - Crie um menu de um sistema de RH que contém as opções:

# 1 - Cadastro de Vendedor
# 2 - Cadastro de Gerente
# 3 - Cadastro de Cliente

# Para o vendedor peça as informações nome, cpf, idade e cidade
# Para o gerente peça as informações nome, cpf, idade, cidade e salario
# Para o cliente peça as informações nome, cpf, idade, endereço e telefone

ascii_logo = r"""
   _____ ___  ____  _____ _____ ______ __  __          _____  _____  _   _  _   _ 
  / ____|__ \|  _ \|  __ \_   _|  ____|  \/  |   /\   |  __ \|  __ \| \ | || \ | |
 | (___    ) | |_) | |__) || | | |__  | \  / |  /  \  | |  | | |__) |  \| ||  \| |
  \___ \  / /|  _ <|  ___/ | | |  __| | |\/| | / /\ \ | |  | |  _  /| . ` || . ` |
  ____) |/ /_| |_) | |    _| |_| |____| |  | |/ ____ \| |__| | | \ \| |\  || |\  |
 |_____/|____|____/|_|   |_____|______|_|  |_/_/    \_\_____/|_|  \_\_| \_||_| \_|

                        SISTEMA DE GESTÃO DE RECURSOS HUMANOS
"""
print(ascii_logo)


print("Seja bem vindo ao sistema!")

print('''
      
Escolha uma das opções do menu abaixo:
      
      1. Cadastrar Vendedor
      2. Cadastrar Gerente
      3. Cadastrar Cliente

''')

op = input("Digite o número da opção desejada: ")

if op == "1":
    nome = input("Digite o nome do vendedor: ")
    cpf = input("Digite o CPF do vendedor: ")
    idade = int(input("Digite a idade do vendedor: "))
    cidade = input("Digite a cidade do vendedor: ")

elif op == "2":
    nome = input("Digite o nome do gerente: ")
    cpf = input("Digite o CPF do gerente: ")
    idade = int(input("Digite a idade do gerente: "))
    cidade = input("Digite a cidade do gerente: ")
    salario = float(input("Digite o salário do gerente: "))
    
elif op == "3":
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    endereco = input("Digite o endereco do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
else:
    print("Opção inválida. Por favor, tente novamente.")