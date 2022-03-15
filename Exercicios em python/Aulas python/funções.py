'''def linha():
    print('-'*25)

linha()
print('     VASCO DA GAMA')
linha()'''


'''def tema(msg):
    print('-'*25)
    print(msg)
    print('-'*25)

tema('   APRENDENDO PYTHON')
tema('   Vasco x Flamengo')'''




'''def soma(a, b):
    s = a + b
    print(s)

#programa principal
soma(1, 5)
soma(9, 10)
soma(12, 4)'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'{a} + {b} = {s}')
    
soma(5, 8)'''

'''def contador(* núm):
    for valor in núm:
        print(f'{valor} ',end='')
    print('[FIM!]')'''

'''def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} valores')

contador(2, 1, 7)
contador(8, 0)
contador(9, 2, 3)'''


'''def dobra(lista):
    pos = 0
    while pos < len(valores):
        lista[pos] *= 2
        pos += 1


valores = [8, 3, 4, 6, 7]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for núm in valores:
        s += núm
    print(f'A soma dos {valores} é {s}')


soma(5, 8)
soma(2, 9, 4)