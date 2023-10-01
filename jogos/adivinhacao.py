import random

print("*********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1

print(numero_secreto)
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativas ", rodada, "de ", total_de_tentativas)
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue



    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Seu chute foi maior do que o número secreto!")
            print("Você errou!")
        if menor:
            print("Seu chute foi menor do que o número secreto!")
print("Fim do Jogo!")
