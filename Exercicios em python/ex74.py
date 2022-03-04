from random import randint
gerador_num = randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)
print('Os valores sorteados foram:', end=' ')
for c in gerador_num:
    print(c, end=' ')

print(f'\nO maior valor sorteado foi: {max(gerador_num)}')
print(f'O menor valor sorteado foi: {min(gerador_num)}')