preco = float(input("Qual o preço do produto?"))
desconto = (preco * 5) / 100
total = preco - desconto
print("O valor do produto é R${:.1F} e com deconto de 5% ficará apenas {}".format(preco, total))