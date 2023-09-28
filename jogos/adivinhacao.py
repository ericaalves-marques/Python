print("*********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

while total_de_tentativas > 0:
    chute = input("Digite o seu número: ")

    print("Você digitou ", chute)
    chute = int(chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
    else:
        if maior:
            print("Seu chute foi maior do que o número secreto!")
            print("Você errou!")
        if menor:
            print("Seu chute foi menor do que o número secreto!")
        print("Fim do Jogo!")
