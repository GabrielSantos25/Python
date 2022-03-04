print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 35, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}R$',end='')
    else:
        print(f'{listagem[c]:>7.2f}')
print('-'*40)