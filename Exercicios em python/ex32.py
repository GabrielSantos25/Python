ano = int(input('Informe um ano(4digitos): '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Não é Bissexto')