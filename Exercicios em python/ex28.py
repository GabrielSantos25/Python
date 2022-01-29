import random
from time import sleep
print('Jogo da Adivinhação')
jogo = int(input('Escolha um número inteiro entre 0 a 5: '))
maquina = random.randint(0, 5)
print('Processando...')
sleep(2)
if jogo == maquina:
    print('Você acertou, Parabéns!')
else:
    print('Você perdeu, Tente novamente!')
print('O número sorteado foi: {}'.format(maquina))