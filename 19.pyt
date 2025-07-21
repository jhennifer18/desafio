def jogo_adivinhacao(numero_secreto):
    while True:
        palpite = int(input("Digite seu palpite: "))
        if palpite < numero_secreto:
            print("Maior que o número secreto.")
        elif palpite > numero_secreto:
            print("Menor que o número secreto.")
        else:
            print("Parabéns! Você acertou!")
            break
