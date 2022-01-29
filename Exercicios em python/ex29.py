km = int(input('Qual a velocidade do carro? '))
if km > 80:
    multa = (km - 80) * 7
    print('Você foi multado, limite de 80km ultrapassado!')
    print('A multa custa R$7,00 por KM ultrapassado, você pagará: {:.2f}'.format(multa))