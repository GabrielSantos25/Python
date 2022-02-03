#dedector de palíndromo
from posixpath import split
frase = str(input('Escreva uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
