# faça um programa que leia a altura e largura de uma parede e calcule sua area
# e a quantidade de tinta necessaria para pita-la.
# considere cada litro de tinta pinta 2 metros quadrados

print('=' * 10, ' Cáuculo de área e quantidade de tinta ', '=' * 10)
a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
ar = a * l
t = ar / 2
print(f'\nA área da parede é de {ar:.2f}m²: e serão necessarios {t:.2f} \nlitros de tinta para pinta-la!')
# repare que na linha anterior foi usado uma nova forma de usar o .format de maneira mais simplificada.
print('=' * 61)     # Essa linha é apenas para printar uma linha, o codigo funciona normal sem ela.