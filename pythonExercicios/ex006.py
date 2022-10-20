# Escreva um programa que receba um numero, diga seu dobro seu tripulo e sua raiz quadrada.

num = int(input('Digite um numero: '))
print('O dobro de {} vale {}.\n O tripulo de {} vale {}. \n A raiz quadrada de {} vale {:.2f}.'.format(num, (num * 2), num, (num * 3), num, (num **(1/2))))
