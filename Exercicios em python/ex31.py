from dis import dis


dist = int(input('Qual vai ser a distancia da viagem em Km: '))
curta = 0.50
longa = 0.45
if dist <= 200:
    menor = curta * dist
    print('Simulação do orçamento: R${:.2F}'.format(menor))
else:
    maior = longa * dist
    print('Simulação do orçamento: R${:.2F}'.format(maior))