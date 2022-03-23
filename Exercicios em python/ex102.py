fila1 = list()
fila2 = list()
fila3 = list()
fila4 = list()
while True:
    while True:
        for f1 in range(1):
            fila1.append(int(input('N: ')))
    
    
        for f2 in range(1):
            fila2.append(int(input('N: ')))
    
        for f3 in range(1):
            fila3.append(int(input('N: ')))
        
        for f4 in range(1):
            fila4.append(int(input('N: ')))
            
        if len(fila1) == 3:
            break    

    if len(fila1) == 3:
        break

fila1.reverse()
fila2.reverse()
fila3.reverse()
fila4.reverse()

# FILA 1 (Saida)
print('-='*10)
print('FILA 1')
print('-='*10)
for a in range(3):
    print(fila1)
    fila1.pop()
print(fila1)

# FILA 2 (Saida)
print('-='*10)
print('FILA 2')
print('-='*10)
for b in range(3):
    print(fila2)
    fila2.pop()
print(fila2)

#FILA 3 (Saida)
print('-='*10)
print('FILA 3')
print('-='*10)
for c in range(3):
    print(fila3)
    fila3.pop()
print(fila3)

# FILA 4 (Saida)
print('-='*10)
print('FILA 4')
print('-='*10)
for d in range(3):
    print(fila4)
    fila4.pop()
print(fila4)

