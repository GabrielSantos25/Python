extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente.',end=' ')
print(f'Você digitou o número {extenso[escolha]}')