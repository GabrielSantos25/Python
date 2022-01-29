salario = float(input('Informe seu salário: '))
if salario > 1250:
   ajuste = 0.10 * salario
   ajuste += salario
   print('O seu salário de R${:.2f} sofreu aumento de 10%. Reajuste salárial: R${:.2f}'.format(salario, ajuste))

else:
    ajuste = 0.15 * salario
    ajuste += salario
    print('O seu salário de R${:.2f} sofreu aumento de 15%. Reajuste salárial: R${:.2f}'.format(salario, ajuste))
