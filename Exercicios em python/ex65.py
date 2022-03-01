n = x = m = s = tot = 0
maior = menor = 0
while x != 'N':
    if n != 'N':
        n = int(input('Digite um número: '))
        x = str(input('Quer continua? [S/N]')).upper()
        tot += 1
        s += n
        m = s / tot
    if tot == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
print(f'Você digitou {tot} números e a média foi {m}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

        
   