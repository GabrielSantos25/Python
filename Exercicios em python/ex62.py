#Melhorada progressão aritmética em while
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
primeiro = termo
cont = 1
novo = 10
total = 0
while novo != 0:
    total += novo
    while cont <= total:
        print(f'{primeiro}', end=' -> ')
        primeiro += razao
        cont += 1
    print('Acabou')
    novo = int(input('Quer mostrar mais termos? '))
print(f'Progressão finalizada com {total} termos ao todo')