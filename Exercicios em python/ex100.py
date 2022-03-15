from random import randint

def sorteia(sorteio):
    for c in range(0, 5):
        numeros.append(randint(1, 50))
    print(numeros)


def somaPar(sorteio):
    s = 0
    for valor in sorteio:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores {sorteio}, temos {s}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
