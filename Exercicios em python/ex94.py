grupo = list()
dados = dict()
soma = média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Por faver, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    grupo.append(dados.copy())
    while True:
        resp = str(input('Quer continuar (S/N)? ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-='*30)
#Quantos pessoas foram cadastradas!
print(f'A) O grupo tem {len(grupo)} pessoas.')

#Descobrir a média de idade entre as pessoas cadastradas!
média = soma / len(grupo)
print(f'B) A média de idade é de {média:5.2f}')

#Descobrir os nomes das mulheres cadastradas!
print('C) As mulheres cadastradas foram: ', end='')
for m in grupo:
    if m['sexo'] == 'F':
        print(f'[{m["nome"]}] ', end='')
print()

#Descobrir pessoas acima da média!
print('D) Lista das pessoas que estão acima da média: ',end='')
for p in grupo:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'    [{k} = {v}]; ', end='')
        print()
print('-='*30)
print('<<<Encerrado>>')