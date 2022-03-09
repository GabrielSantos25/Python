lista = []
teste = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    # SABER MAIOR OU MENOR!
    if len(teste) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
            
    resp = ' '
    teste.append(lista[:])
    lista.clear()

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] 
    if resp == 'N':
        break
    
  
print(f'Ao todo, você cadastrou {len(teste)} pessoas.')

print(f'O maior peso foi de {maior}kg. Peso de ',end='')
for pessoa in teste:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()

print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for pessoa in teste:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')