nascimento = int(input('Informe sua idade: '))

if nascimento < 18:
    resta = 18 - nascimento
    print('Ainda vai se alista, falta apenas {} ano(s).'.format(resta))
elif nascimento == 18:
    print('hora de se alistar.')
elif nascimento > 18:
    passou = nascimento - 18
    print('Passou do tempo, já se foram {} ano(s).'.format(passou))
    
    
