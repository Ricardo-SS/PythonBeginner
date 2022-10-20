#criar um programa que leia um angulo e mostre o valor do seu seno, coseno e tangente;
from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo em graus: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

