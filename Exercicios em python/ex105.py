from datetime import date
dados = list()
atual = date.today().year
arquivo = open("stats.txt", "a")
while True:
    nome = str(input('Nome: ')).title()[0: 40]
    anonas = int(input('Ano de Nascimento: '))
    idade = atual - anonas

    if idade < 18:
        resultado = "Menor de Idade"
    if idade > 18:
        resultado = "Maior de Idade"
    if idade == 18:
        resultado = "Entrando na maior idade"
    resp = str(input('Quer continuar [S/N]: '))
    
    dados.append([nome, anonas, idade, resultado])
    
    if resp in "Nn":
        break
    
    
for r in range(len(dados)):
    arquivo.writelines(f'--- {r+1}ª Indivíduo ---\nNome: {dados[r][0]}\nAno de nascimento: {dados[r][1]}\nIdade: {dados[r][2]}\nResultado: {dados[r][3]}\n\n')