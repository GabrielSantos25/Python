dados = dict()

dados['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = 0
idade = 2022 - ano_nascimento
dados['Idade'] = idade
dados['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Ctps'] > 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    aposentadoria = (dados['Contratação'] + 35) - ano_nascimento
    dados['Aposentadoria'] = aposentadoria
print(dados)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')