nome = str(input('Escreva seu nome completo: '))
print('Nome:', nome)
print('Seu nome com todas letras Maiúsculo:',nome.upper())
print('Seu nome com todas letras Minúsculas:', nome.lower())
dividido = nome.split()
print('Quantas letras tem seu nome:', len(''.join(dividido)))
print('Quantas letras tem seu primeiro nome:', len(dividido[0]))