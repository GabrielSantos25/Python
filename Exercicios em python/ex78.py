valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))

print('=='*30)
print(f'Os valores digitados foram {valores}')
for p , v in enumerate(valores):
    if v == max(valores):
        print(f'O maior valor foi {max(valores)} na posição {p}')
    if v == min(valores):
        print(f'O menor valor foi {min(valores)} na posição {p}')