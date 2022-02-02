import random
from time import sleep
print('\033[1;97mSuas opções:\033[m')
print('\033[1;31m[PEDRA]\n[PAPEL]\n[TESOURA]')
jogador = str(input('\033[1;97mQual é a sua jogada?\033[m ')).upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = random.choice(lista)


sleep(1)
print('\033[1;33mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;33mPO!!!\033[m')
sleep(2)


print('\033[1;97m-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Computador jogou {}'.format(maquina))
print('Jogador jogou {}'.format(jogador))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=')


if jogador == maquina:
    print('\033[1;32mEMPATE\033[m')
# Ganhador jogador
elif jogador == 'PEDRA' and maquina == 'TESOURA':
    print('\033[1;32mJogador venceu!\n{} vs {} = {}\033[m'.format(jogador, maquina, jogador))

elif jogador == 'TESOURA' and maquina == 'PAPEL':
    print('\033[1;32mJogador venceu!\n{} vs {} = {}\033[m'.format(jogador, maquina, jogador))

elif jogador == 'PAPEL' and maquina == 'PEDRA':
    print('\033[1;32mJogador venceu!\n{} vs {} = {}\033[m'.format(jogador, maquina, jogador))

# Ganhador maquina
elif maquina == 'PEDRA' and jogador == 'TESOURA':
    print('\033[1;32mComputador venceu!\n{} vs {} = {}\033[m'.format(jogador, maquina, maquina))

elif maquina == 'TESOURA' and jogador == 'PAPEL':
    print('\033[1;32mComputador venceu!\n{} vs {} = {}\033[m'.format(jogador, maquina, maquina))

elif maquina == 'PAPEL' and jogador == 'PEDRA':
    print('\033[1;32mComputador venceu!\n{} vs {} = {}\033[m'.format(jogador, maquina, maquina))