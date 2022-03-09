from audioop import reverse
from operator import index
total = pos = 0
lista = []
while True:
    num = int(input('Digite um valor: '))
    total += 1
    resp = ' '
    lista.append(num)
    lista.sort(reverse=True)
      
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':
        break

posição = lista.index(5)

print(f'Você digitou {total} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista e se encontra na posição {posição}ª!')
else:
    print('O valor 5 não foi encontrado na lista!')