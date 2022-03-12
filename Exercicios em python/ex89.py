from statistics import median

lista = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota1: ')))
    temp.append(float(input('Nota2: ')))
    lista.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]: ')).upper()
    
    if resp == 'N':
        break

print('-='*25)
print(f'No. NOME        MÉDIA:')
print('-'*25)
for c in range(0, len(lista)):
    print(f'{c:^2}  {lista[c][0]}{median(lista[c][1:]):^20}')
    

while True:
    for aluno in range(0, len(lista)):
        aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        print(lista[aluno][1:])
    if aluno == 999:
        break
   