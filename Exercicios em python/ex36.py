valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Quantos anos vai pagar: '))

prestacao_m = valor / (anos * 12)
renda = salario * 0.30

if prestacao_m <= renda:
    print('Emprestimo Aprovado!')
else:
    print('Emprestimo Negado!')

print('Para pagar a casa de R${:.2f} em {} anos a prestação será R${:.2f}. Não corresponde 30% do seu salario que é R${:.2f}.'.format(valor, anos, prestacao_m, renda))
        