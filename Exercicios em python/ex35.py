from statistics import median


r1 = int(input('Reta1: '))
r2 = int(input('Reta2: '))
r3 = int(input('Reta3: '))

lista = []
lista.append(r1)
lista.append(r2)
lista.append(r3)

if (min(lista) + median(lista)) > max(lista):
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo!')