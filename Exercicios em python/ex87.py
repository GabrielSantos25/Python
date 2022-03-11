spar = sc3 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Num {l} e {c}: '))
        #Soma de todos os pares digitados
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
            
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()

#Soma da terceira coluna
for l in range(0, 3):
    sc3 += matriz[l][2]

print(f'A soma de todos os pares: {spar}')
print(f'Soma dos valores da terceira coluna: {sc3}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')