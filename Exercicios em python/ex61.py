#Progressão aritmética em while
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
primeiro = termo
cont = 1
while cont <= 10:
    print(f'{primeiro}', end=' -> ')
    primeiro += razao
    cont += 1
print('Acabou')