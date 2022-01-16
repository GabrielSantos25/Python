largura = int(input("Digite a Largura da parede: "))
altura = int(input("Digite a Altura da parede: "))
area = largura * altura
tinta = (largura * altura)/ 2
print("A parede possui {} de largura e {} de altura, sua area equivale à {}. Serão necessarios {}litros de tintas para pinta-lá".format(largura, altura, area, tinta))