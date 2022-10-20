#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#numero = str(input('Digite um número de 0 a 9999: '))

num = int(input('Digite um núero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número: {}'.format(num))
print('Unidade(s): {}'.format(u))
print('Dezenas(s): {}'.format(d))
print('Centenas(s): {}'.format(c))
print('Unidades(s): {}'.format(m))
