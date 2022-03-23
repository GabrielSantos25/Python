dados = list()
s= m = 0
media = 7
arquivo = open("media.txt", "a")
for c in range(3):
    nome = str(input('Nome: '))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    s = nota1 + nota2
    m = s / 2
    print('-'*20)

    if m >= media:
        resultado = ('Aprovado')
    else:
        resultado = ('Reprovado')


    dados.append([nome, nota1, nota2, m, resultado])
    
for x in range(len(dados)):
    arquivo.writelines(f'---Aluno {x+1}ª---\nNome: {dados[x][0]}\nNota1: {dados[x][1]}\nNota2: {dados[x][2]}\nMedia: {dados[x][3]:.1f}\nResultado: {dados[x][4]}\n')