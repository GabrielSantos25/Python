#repetição
for c in range(0, 10):
    num = int(input('informe um num: '))
print('FIM')

#estrutura for range()
for c in range(7, 0, -1):
    print(c)

#estrutura com variavel for range()
inicio = int(input('num: '))
meio = int(input('num: '))
fim = int(input('num: '))

for c in range(inicio, meio, fim):
    print(c)


#somatorio com for
s = 0
for c in range(0, 5):
    num = int(input(''))
    s += num
print('O somatório dos números foi:',s)
print('FIM')