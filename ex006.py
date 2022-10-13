# Escreva um programa que receba um numero, diga seu dobro seu tripulo e sua raiz quadrada.

import math

num = int(input("Digite um número inteiro: "))
print("O dobro de {} é {}" .format(num, (num*2)))
print("O tripulo de {} é {}" .format(num, (num*3)))
print("A raiz quadrada de {} é {:.4f}" .format(num, math.sqrt(num)))
