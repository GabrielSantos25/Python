tupla = ('python', 'estudar', 'linguagem', 'curso', 'viajar',
         'cinema', 'pipoca', 'futuro', 'programador', 'mercado')


for c in tupla:
    print(f'\nNa palavra {c} temos as vogais:', end=' ')
    for vogais in c:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
