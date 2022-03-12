from random import randint
from time import sleep


quant_jogos = int(input('Quantos jogos? '))
for c in range(0, quant_jogos):
    palpites = []
    while len(palpites) != 6:
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
    print(f'Jogo {c + 1}: {sorted(palpites)}')
    sleep(1)