preço = float(input('Informe o preço normal: '))
condição = int(input('Informe a condição de pagamento:\n[1]- Dinheiro/cheque\n[2]- Cartão\n[3]- Cartão(2x)\n[4]- Cartão(3x ou +)\nSua Opção:'))

if condição == 1:
    dinheiro = preço - (preço * 0.10)
    print('Pagando á vista você recebe um desconto de 10%, o valor final do item será R${:.2f}'.format(dinheiro))

elif condição == 2:
    dinheiro = preço - (preço * 0.05)
    print('Pagando no cartão você recebe um desconto de 5%, o valor final do item será R${:.2f}'.format(twox, dinheiro))

elif condição == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}, O valor final do item: R${:.2f}'.format(parcela ,preço))

elif condição == 4:
    parcela = int(input('Quantas parcelas: (3x ou +)\nInforme:'))
    juros = (preço / parcela) + (preço * 0.20) / parcela
    final = preço + (preço * 0.20)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS\nSua compra de R${:.2f} vai custar R${:.2f} no final'.format(parcela, juros, preço, final))

else:
    condição = 0
    print('Opção invalida de pagamento')
    