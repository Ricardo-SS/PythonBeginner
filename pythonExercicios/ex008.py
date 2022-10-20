# Escreva um programa que receba a medida em metros e coverta em centimetros e milinmetros

print('=' * 10, ' Conversor de medidas: ', '=' * 10)
medida = float(input('Digite os metros: '))
cm = medida * 100
mm = medida * 1000
print('{} metros tem: \n{}cm \n{}mm' .format(medida, cm, mm))
