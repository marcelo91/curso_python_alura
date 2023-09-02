import adivinhacao
import forca

def escolher_jogo():
    print("************************************")
    print("**** Escolha o Jogo ****")
    print("************************************")

    print('(1) jogo da forca, (2) para o jogo de adivinhação')
    jogo = int(input('Digite o jogo'))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando adivinhação')
        adivinhacao.jogar()
    print('Fim de jogo!!!')

if(__name__ == '__main__'):
    escolher_jogo()
