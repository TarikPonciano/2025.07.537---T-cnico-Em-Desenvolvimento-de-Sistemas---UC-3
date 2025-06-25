# Cenário 3 - Crie um sistema de lanchonete que exibe na tela pelo menos 5 opções de lanche contendo Código, Nome e Preço. Peça para que o usuário digite o código do lanche e a quantidade desejada. Exiba na tela o valor total da compra. (Crie uma notinha fiscal com nome do produto, quantidade e valor total)

print("Bem vindo à Pará Lanches")

print('''
Escolha um item do cardápio:
      
      1 - Hamburguer - R$ 10,00
      2 - Pizza - R$ 15,00
      3 - Hot-Dog - R$ 10,00
      4 - Suco de Laranja 300ml - R$ 10,00
      5 - Coca Zero Lata - R$ 5,99 

''')

op = input("Digite o código do item desejado: ")

# Caso quiser validar se o op é válido
# if op in ["1","2","3","4","5"]:
#     qtd = int(input("Digite a quantidade desejada: "))
#     # DAR CONTINUIDADE AO CÓDIGO AQUI
# else:
#     print("Código inválido!")
#     exit()

qtd = int(input("Digite a quantidade de unidades desejada: "))

if op == "1":
    nome = "Hamburguer"
    preco = 10.00
elif op == "2":
    nome = "Pizza"
    preco = 15.00
elif op == "3":
    nome = "Hot-Dog"
    preco = 10.00
elif op == "4":
    nome = "Suco de Laranja 300ml"
    preco = 10.00
elif op == "5":
    nome = "Coca Zero Lata"
    preco = 5.99
else:
    print("Código informado é inválido!")
    nome = "PRODUTO INVÁLIDO"
    preco = 0
    qtd = 0

total = preco * qtd

print(f"Você comprou {qtd} unidades de {nome}. O total da sua conta é: R$ {total:.2f}")