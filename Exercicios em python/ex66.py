tot = s = num = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    tot += 1
    s += num
print(f'A soma dos {tot} valores foi {s}')
        
    