nome = str(input('Qual é seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Carlos':
    print('Seu nome é popular no Brasil!')
elif nome in 'Cláudia Ana Clara Stela':
    print('Belo nome feminino')         
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))