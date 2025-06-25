#Crie um programa que possui uma variável chamada numeroSecreto. Atribua um valor de 0 a 10 a essa variável. Faça um programa que pergunta ao usuário um palpite de 0 a 10 e verifique se ela acertou ou errou o palpite. 
#Se o usuário errar, informe se o palpite é maior ou menor que o número secreto.
#Permita que a pessoa tente 3 vezes antes de acabar o jogo.
import random

while True:
    numeroSecreto = random.randint(0, 100)

    # Nível 1
    # if palpite == numeroSecreto:
    #     print("Parabéns, você acertou o número secreto!")
    # else:
    #     print("Que pena, você errou o número secreto!")

    # Nível 2

    # if palpite == numeroSecreto:
    #     print("Parabéns, você acertou o número secreto!")
    # elif palpite > numeroSecreto:
    #     print("Que pena, você errou o número secreto! O número secreto é menor!")
    # elif palpite < numeroSecreto:
    #     print("Que pena, você errou o número secreto! O número secreto é maior!")

    # Nível 3

    # if palpite == numeroSecreto:
    #     print("Parabéns, você acertou o número secreto!")
    # else:
    #     if palpite > numeroSecreto:
    #         print("Que pena, você errou o número secreto! O número secreto é menor!")
    #     else:
    #         print("Que pena, você errou o número secreto! O número secreto é maior!")
        
    #     print("Tente novamente!")
    #     palpite = int(input("Segunda Tentativa! Digite um número de 0 a 10: "))

    #     if (palpite == numeroSecreto):
    #         print("Parabéns, você acertou o número secreto!")
    #     else:
    #         if (palpite > numeroSecreto):
    #             print("Que pena! Você errou! O número secreto era menor!")
    #         else:
    #             print("Que pena! Você errou! O número secreto era maior!")
            
    #         print("Tente Novamente!")

    #         palpite = int(input("Terceira Tentativa! Digite um número de 0 a 10"))

    #         if(palpite == numeroSecreto):
    #             print("Parabéns, você acertou na última tentativa!")
    #         else:
    #             print(f"FIM DE JOGO! O número secreto era: {numeroSecreto} ")

    # Nível 4

    tentativas = 0

    while True:
        while True:
            palpite = int(input("Digite um número de 0 a 100: "))
            if palpite >= 0 and palpite <= 100:
                break

        tentativas += 1

        if palpite == numeroSecreto:
            print("Parabéns, você acertou o número secreto!")
            break

        elif palpite > numeroSecreto:
            print("Que pena, você errou o número secreto! O número secreto é menor!")
        elif palpite < numeroSecreto:
            print("Que pena, você errou o número secreto! O número secreto é maior!")
        
        if tentativas >= 3:
            print(f"FIM DE JOGO! O número secreto era: {numeroSecreto} ")
            break

    continuar = input("Deseja continuar? (S/N)")

    if continuar == "N":
        break


            


