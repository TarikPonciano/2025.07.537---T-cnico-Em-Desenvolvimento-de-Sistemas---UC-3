#Cenário 3 - Crie um programa que simula um caixa eletrônico e pede ao usuário o valor de um saque em dinheiro físico e exibe na tela o número de notas de 100, 50, 20, 10, 5 e 2 reais necessárias para completar a transação. Caso haja restante, exiba como troco.
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0

valorOriginal = float(input("Digite o valor que deseja sacar: "))
valorRestante = valorOriginal

if valorRestante >= 100:
    notas100 = int(valorRestante / 100)
    valorRestante = valorRestante - (notas100 * 100)

if valorRestante >= 50:
    notas50 = int(valorRestante / 50)
    valorRestante = valorRestante - (notas50 * 50)

if valorRestante >= 20:
    notas20 = int(valorRestante / 20)
    valorRestante = valorRestante - (notas20 * 20)

if valorRestante >= 10:
    notas10 = int(valorRestante / 10)
    valorRestante = valorRestante - (notas10 * 10)

if valorRestante >= 5 and valorRestante % 2 != 0:
    notas5 = int(valorRestante / 5)
    valorRestante = valorRestante - (notas5 * 5)

if valorRestante >= 2:
    notas2 = int(valorRestante / 2)
    valorRestante = valorRestante - (notas2 * 2)

print(f'''
------ Detalhes do Saque ------
      
Para sacar o valor de R$ {valorOriginal:.2f} as notas utilizadas foram:
      
{notas100} - notas de 100
{notas50} - notas de 50
{notas20} - notas de 20
{notas10} - notas de 10
{notas5} - notas de 5
{notas2} - notas de 2

Troco: R$ {valorRestante:.2f}


''')