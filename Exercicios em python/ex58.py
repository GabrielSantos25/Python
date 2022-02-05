from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

palpite = 0
#Criando o laço!
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpite += 1

    #Quando o jogador acertar a escolha, a repetição [PARA]!
    if jogador == computador:
        acertou = True

    #Se não acerta continua, com especificações!
    else:
        if jogador < computador:
            print('[Mais] tente mais uma vez.')
        elif jogador > computador:
            print('[Menos] tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpite))

