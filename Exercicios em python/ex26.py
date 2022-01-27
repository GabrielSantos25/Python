nome = str(input('Escreva seu nome completo: ')).strip().title()
lista = nome.split()
print('Qual seu primeiro nome: {}'.format(lista[0]))
print('Qual seu último nome: {}'.format(lista[len(lista)-1]))