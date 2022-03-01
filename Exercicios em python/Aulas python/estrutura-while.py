'''for c in range(1, 10):
    print(c)
print('FIM')'''
# pode usar while ou for quando sabemos o limite da repetição

#crescente
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

# while decrescente
n = int(input('Digite um número para\nCalcular seu fatorial: '))
c = n
while c > 0:
    print(c)
    c -= 1

# Somente o while quando não sabemos o limite da repetição
n = 1
while n != 0:
    n = int(input('teste: '))
print('boa')

# exemplo 2
n = 1
r = 'S'
while r == 'S':
    n = int(input('Informe um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('fim')

# exemplo 3

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par,impar))