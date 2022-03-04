times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'America-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

posição = times.index('Chapecoense')

print('=-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('=-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=-='*15)
print(f'Os 4 últimos são: {times[17:21]}')
print('=-='*15)
print(f'Times na ordem alfabética: {sorted(times)}')
print('=-='*15)
print(f'O {times[20]} está na {posição}ª posição')
