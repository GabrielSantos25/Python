x = 0
lista = []
resp = ''
while True:
    x = int(input('Digite um valor: '))
    if x not in lista:
        lista.append(x)
        print('Adicionado com sucesso')
    else:
        print('Valor duplicado, não irei adicionar')
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(lista)
    