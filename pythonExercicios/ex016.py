#criar um programa que leia um numero real qualquer e mostre sua parte inteira.
from math import floor
numero = float(input('Digite um número real: '))
print('A parte inteira de {} é igual a {}:'.format(numero, floor(numero)))
