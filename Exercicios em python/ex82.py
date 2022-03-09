lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
    
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        lista_par.append(lista[c])
    elif lista[c] % 2 == 1:
        lista_impar.append(lista[c])


print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')