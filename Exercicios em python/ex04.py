msg = input('Digite algo: ')

print('Informações de {}'.format(msg))
print('Tipo', type(msg))
print('Alfabetico:', msg.isalpha())
print('Numérico:', msg.isnumeric())
print('Alfanumérico', msg.isalnum())