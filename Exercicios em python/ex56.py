#Analisador completo
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenor20 = 0
for p in range (1, 5):
    print('---- {} PESSOA ----'.format(p))
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).upper()
    
    #Media da idade do grupo
    somaidade += idade

    #O nome do homem mais velho
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    else:
        if sexo in 'M' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome

    #Quantas mulhers tem menos de 20 anos
    if sexo == 'F':
        if idade < 20:
            mulhermenor20 += 1

mediaidade = somaidade / 4

print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulhermenor20))