boletim = dict()
lista = list()
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))

for k, v in boletim.items():
    print(f'{k} é igual a {v}')

if boletim['Média'] >= 7:
    print(f'Situação do aluno {boletim["Nome"]}, "Aprovado"')
elif boletim['Média'] >= 4 and boletim['Média'] < 7:
    print(f'Situação do aluno {boletim["Nome"]}, "Recuperação"')
if boletim['Média'] >= 0 and boletim['Média'] < 4:
    print(f'Situação do aluno {boletim["Nome"]}, "Reprovado"')