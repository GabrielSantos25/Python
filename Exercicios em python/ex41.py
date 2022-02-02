ano = int(input('Informe seu ano de nascimento: '))

if ano >=0 and ano <= 9:
    print('Categoria: MIRRIM')
elif ano >= 10 and ano <= 14:
    print('Categoria: INFANTIL')
elif ano >= 15 and ano <= 19:
    print('Categoria: JUNIOR')
elif ano == 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
    