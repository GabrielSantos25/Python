nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
lista = list()
dados = dict()
for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
dados['Nome'] = nome
dados['Gols'] = lista
dados['Total'] = partidas
print('-='*20)
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {nome} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'  => Na partida {c}, fez {lista[c]} gols.')
print(f'Foi um total de {sum(lista)} gols.')