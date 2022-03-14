from audioop import reverse
from operator import itemgetter
from random import randint
from time import sleep


dados = {'Jogador1': randint(1, 6), 'Jogador2': randint(
    1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = dict()
print('=== Valores sorteados: ===')
for k, v in dados.items():
    print(f'   O {k} tirou {v}')

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('=== Ranking dos jogadores: ===')
for i, v in enumerate(ranking):
    print(f'   {i+1}ª lugar: {v[0]} com {v[1]}')
