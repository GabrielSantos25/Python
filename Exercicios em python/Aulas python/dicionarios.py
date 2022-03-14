#dicionarios.values() retorna valores
#dicionarios.keys() retorna título
#dicionarios.items() retorna título e valores
'''teste = dict()'''


'''dados = {'nome':'gabriel', 'idade': 25 }
print(dados['nome'])
print(dados['idade'])
for k, v in dados.items():
    print(f'o {k} é {v}')'''
    

'''teste = [{'Título': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}, {'Título': 'Vigadores', 'Ano': 2019, 'Diretor': 'Marvel'} ]
print(teste[1]['Ano'])'''

estado = dict()
brasil = list()
for c in range(0, 2):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SG'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')'''
        
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()