def tema(str):
    print(str)
    print('-'*20)
tema('CONTROLE DE TERRENOS')
comprimento = float(input('LARGURA (m): '))
largura = float(input('COMPRIMENTO (m): '))

def área(largura, comprimento):
    calculo = comprimento * largura
    print(f'A área do terreno [{largura} x {comprimento}] é {calculo}m²')


área(comprimento, largura)