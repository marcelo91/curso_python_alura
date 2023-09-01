def jogar():
    print("************************************")
    print("****Bem vindo ao jogo da forca!****")
    print("************************************")

    # minha palavra secreta, e (upper)deixando maiusculo
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    # enquanto variaveis (enforcou e acertou) são falsas faça:
    while not enforcou and not acertou:
        # pegando palavra dada pelo usuário
        chute = input("Qual letra você escolhe?")
        # (strip)tirando os espaços da palavra caso existam e (upper)deixando maiusculo
        chute = chute.strip().upper()
        # definindo um index para que possa mostrar a posição da letra dentro da palavra
        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                # condição de acerto e transformação em maiusculo
                if chute == letra:
                    # inserir a letra mencionada na posição correta da palavra
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1

        print(letras_acertadas)

        #logicas para saida do while
        enforcou = erros == 6
        acertou = ("_") not in letras_acertadas

        print("Jogando!!!")

    if acertou:
        print("Ganhou!!!")
    else:
        print("Perdeu!!!")
    print("Fim de jogo!!!")


if __name__ == "__main__":
    jogar()
