#Melhorando o ex9!
num = int(input("Digite um número: "))

print("Tabuada de {}".format(num))
for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num*c))
