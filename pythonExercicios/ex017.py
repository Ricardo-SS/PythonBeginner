#criar um programa que leia o cateto oposto e o cateto adjacente de um triangulo e calcule o valor da hipotenusa.
# hypot é a funcao que calcula o valor da hipotenusa de um triangulo retangulo
from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hipo = hypot(catop, catad)
print('O valor da hipotenusa é igual a {:.2f} '.format(hipo))
