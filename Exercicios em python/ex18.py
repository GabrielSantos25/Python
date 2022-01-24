import math
angulo = float(input('Digite o ângulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

'testando personalização'
from math import sin, radians, cos, tan
angulo = float(input('Digite o ângulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

