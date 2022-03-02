print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cédula = 50
totcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédula de R${cédula:.2f}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totcéd = 0
        if total == 0:
            break
                
print('='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')