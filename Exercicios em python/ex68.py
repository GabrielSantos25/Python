from random import randint

vitoria = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    jogador = int(input("Digite um valor: "))
    maquina = randint(0, 10)
    escolha = ' '
    escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    soma = jogador + maquina
    print('-'*50)
    print(f'Você jogou {jogador} e o computador {maquina}. Total deu {soma}')
    print('-'*50)
    if escolha == 'P':
        if soma % 2 == 0:
            print("você VENCEU")
            print('=-='*18)
            vitoria += 1
        else:
            print('Você PERDEU')
            print('=-='*18)
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            vitoria += 1
            print('você VENCEU')
            print('=-='*18)
        else:
            print('você PERDEU')
            print('=-='*18)
            break
print(f'Game Over! Você venceu {vitoria} vezes.')
