#Progressão aritmética
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
décimot = termo + (10-1) * razao
for c in range(termo, décimot + razao, razao):
    print('{}'.format(c), end=' -> ')
print('acabou')