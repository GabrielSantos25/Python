r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
    if r1 == r2 == r3:
        print('Triângulo equilátero')
    elif r1 != r2 != r3 != r1:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('Não pode formar um triângulo')
