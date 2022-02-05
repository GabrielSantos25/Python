sexo = str(input('Seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, tente novamente: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))