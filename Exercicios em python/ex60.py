#Calculando fatorial em while
n = int(input('Digite um número para\nCalcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}', end='')

#Calculando fatorial em for
n = int(input('Digite um número para\nCalcular fatorial: '))
f = 1
print(f'Calculo {n}!= ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
print(f'{f}',end='')


#fatorial com import factorial em while
from math import factorial

n = int(input('Digite um número para\nCalcular fatorial: '))
c = n
f = factorial(n)
while c > 0:
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    c -= 1
print(f'{f}')


#fatorial com import factorial em for
from math import factorial

n = int(input('Digite um número para\nCalcular fatorial: '))
f = factorial(n)
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
print(f'{f}')


