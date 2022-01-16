carteira = float(input("Digite quantos R$ você possui: "))
dolar = carteira / 5.64

print("Você possui R${}, equivalente à US${:.2f}".format(carteira, dolar))