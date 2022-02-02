num = int(input('Digite um número: '))
conversao = int(input('#Conversão:\n1-Binário.\n2-Octal.\n3-Hexadecimal.\nSua opção: '))

if conversao == 1:
    print('A conversão do número inteiro {} para binário é {}'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('A conversão do número inteiro {} para Octal é {}'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('A conversão do número inteiro {} para Hexadecimal é {}'.format(num, hex(num)[2:]))

    
    