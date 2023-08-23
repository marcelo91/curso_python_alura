import random

def jogar():

    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    print('(1) Facil 30 tentativas, (2) médio 15 tentativas, (3) dificil 3 tentativas')
    nivel = input('Selecione a dificuldade: ')
    if (nivel == 1):
        contador = 30
    elif (nivel == 2):
        contador = 15
    else:
        contador = 3

    pontos = 1000
    numero_secreto = random.randrange(1,101)
    rodada = 1

    print(numero_secreto)

    for rodada in range (1,contador + 1 ):
        print('rodada {} de {}'.format(rodada,contador))
        chute_str = input("Digite um numero = ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100\n')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        
        if (acertou):
            print('Acertou !!! seus pontos são {} \n'.format(pontos))
            break
        else:
            if (maior):
                print('Errou !!! seu numero é maior que o numero secreto\n')
                if (rodada == contador):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print('Errou !!! seu numero é menor que o numero secreto\n')
                if (rodada == contador):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            dif_erro = abs(numero_secreto - chute)
            pontos = pontos - dif_erro


    print('Fim de jogo!!!')

if(__name__ == '__main__'):
    jogar()
