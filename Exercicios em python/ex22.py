from posixpath import split

num = input('Informe um número entre 0 a 9999: ')
a = num.split()
b = num[3]
c = num[2]
d = num[1]
e = num[0]
print('Unidade:{}'.format(b),'\nDezena:{}'.format(c),'\nCentena:{}'.format(d),'\nMilhar:{}'.format(e))