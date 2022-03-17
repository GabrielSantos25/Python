dados = []
notas = []
medias = []
for c in range(3):
    nome = str(input('Nome: '))
    nota1 = int(input('P1: '))
    nota2 = int(input('P2: '))
    nota3 = int(input('avQ: '))
    media = (nota1 + nota2 + nota3) / 3
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    medias.append(media)
    dados.append([nome, [nota1, nota2, nota3], media])

print('-='*30)
# Média dos alunos!
for x in range(3):
    print(f'A média do {dados[x][0]} é {dados[x][2]:.1f}')
print('-='*30)

# Média da turma!
print(f'A média da turma é {sum(notas) / 3:.1f}')
print('-='*30)

# Maior média!
for m in range(3):
    if dados[m][2] == max(medias):
        print(f'{dados[m][0]} obteve a maior média: ',end='')
print(f'[{max(medias):.1f}]',end='')
print()
print('-='*30)
print('---Fim---')
