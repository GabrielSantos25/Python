n1 = int(input('Primeiro número: '))
n2 = int(input('Primeiro número: '))
opção = 0
soma = (n1 + n2)
multi = (n1 * n2)
while opção != 5:
    print('=-='*10)
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    print('=-='*10)
    opção = int(input('>>>>>Qual é sua opção: '))
    if opção == 1:
        print('O resultado de {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        print('O resultado de {} x {} = {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2 and n2 < n1:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif opção == 4:
        print('Informe novos números')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Primeiro número: '))
print('Fim do programa! Volte sempre.')
