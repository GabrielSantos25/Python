print('=-='*15)
print('SUPERMECADO PAGUE MENOS')
print('=-='*15)
total = totalp = cont = menor = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    resp = ' '
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if preço > 1000:
        totalp += 1
    if resp == 'N':
        break

print('===== FIM DO PROGRAMA =====')
print(f'Total de compra foi R${total:.2f}')
print(f'Temos {totalp} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
