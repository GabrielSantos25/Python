n = 0
totn = 0
s = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        s += n
        totn += 1
       
print(f'Foram digitados {totn} números e o somatório deles é {s}')

