nota1 = float(input('Informe sua primeiro nota: '))
nota2 = float(input('Informe sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Média necessaria: [7.0], sua media foi {:.1f}\nReprovado!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Média necessaria: [7.0], sua media foi {:.1f}\nRecuperação!'.format(media))
elif media >= 7.0:
    print('=--=Parabéns=--= Sua média foi {:.1f}\nAprovado!'.format(media))
        