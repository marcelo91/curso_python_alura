import random


def jogar():
    print("************************************")
    print("****Bem vindo ao jogo da forca!****")
    print("************************************")

    secret_word = random_secret_word()

    letras_acertadas = ["_" for letters in secret_word]

    enforcou = False
    acertou = False
    erros = 0

    # enquanto variaveis (enforcou e acertou) são falsas faça:
    while not enforcou and not acertou:
        # pegando palavra dada pelo usuário
        chute = input("Qual letra você escolhe?").strip().upper()
        # definindo um index para que possa mostrar a posição da letra dentro da palavra
        index = 0
        if chute in secret_word:
            for letra in secret_word:
                # condição de acerto e transformação em maiusculo
                if chute == letra:
                    # inserir a letra mencionada na posição correta da palavra
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1

        print(letras_acertadas)

        # logicas para saida do while
        enforcou = erros == 7
        desenha_forca(erros)
        acertou = ("_") not in letras_acertadas

        print("Jogando!!!")

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(secret_word)


##########FUNCTIONS##########


def random_secret_word():
    word_list = []
    archive = open("entry.txt", "r")
    for line in archive:
        word_list.append(line.strip().upper())
    archive.close()
    return random.choice(word_list)


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
