# faça um programa que leia a altura e largura de uma parede e calcule sua area
# e a quantidade de inta necessaria para pitala.
# considere cada litro de tinta pinta 2 metros quadrados

print('=' * 10, ' Cáuculo de área e quantidade de tinta ', '=' * 10)
a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
ar = a * l
t = ar / 2
print(f'A área da parede é de {ar:.2f}m²: e serão necessarios {t:.3f} litros de tinta para pinta-la!')
