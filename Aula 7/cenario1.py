# Cenário 1 - Crie um menu de atendimento que exibe pelo menos 4 opções de serviços de uma operadora telefônica, peça ao usuário para escolher um item desse menu e exiba uma resposta de acordo com o menu escolhido.

print("Bem vindo ao atendimento da Telefonia XYZ")

print('''
Escolha uma das opções do menu abaixo:
      
1. Obter segunda via da fatura
2. Conferir saldo
3. Cancelar Plano
4. Falar com atendente
0. Sair
      
''')

op = input("Digite o número da opção desejada: ")

if op == "1":
    print("Você solicitou a segunda via da fatura. Em breve você receberá um email com os detalhes!")
elif op == "2":
    print("Você solicitou a conferência do saldo. Em breve você receberá um email com os detalhes!")
elif op == "3":
    print("Para cancelar fale com um de nossos atendentes.")
elif op == "4":
    print("Aguarde...")
elif op == "0":
    print("Obrigado por utilizar o atendimento da Telefonia XYZ!")
    exit()
else:
    print("Opção inválida. Por favor, tente novamente.")