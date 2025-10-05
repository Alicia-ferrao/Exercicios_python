

import math



angulo = int(input('Digite o ângula que deseja : '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))


print('O ângulo de {} tem o seno de {:.2f}' .format(angulo, seno))
print('O angulo de {} tem o seno de {:.2f} ' .format(angulo, cosseno))
print('O angulo de {} tem a tan de {:.2f} '.format(angulo,tan))


