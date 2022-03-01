#Sequencia de fibonacci
n = int(input('Digite um número: '))
c = 3
primeiro = 0
segundo = 1
print(f'{primeiro} -> {segundo} -> ', end='')
while c <= n:
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
    print(f'{terceiro} -> ', end='')
    c += 1
print('FIM')