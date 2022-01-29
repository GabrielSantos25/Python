num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

#MAIOR NÚMERO!
if (num1 > num2) and (num1 > num3):
    print('O maior número é {}'.format(num1))
elif (num2 > num1) and (num2 > num3):
    print('O maior número é {}'.format(num2))
elif (num3 > num1) and (num3 > num2):
    print('O maior número é {}'.format(num3))
else:
    print('Todos são iguais')

#MENOR NÚMERO!
if (num1 < num2) and (num1 < num3):
    print('O menor número é {}'.format(num1))
elif (num2 < num1) and (num2 < num3):
    print('O menor número é {}'.format(num2))
else:
    print('O menor número é {}'.format(num3))
