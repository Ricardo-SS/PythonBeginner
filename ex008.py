# crie um programa conversor de medidas de metros para km, cm, mm

print('-' * 10, ' Conversor de Medidas', '=' * 10) # cria uma linha antes e depois da palavra, o = é repetido o numero de vezes pelo qual é multiplicado

medida = float(input('Digite a quantidade de metros: '))
km = medida * 0.001
cm = medida * 100
mm = medida *1000
print('{} metros tem: \n{} Km \n{} cm \n{} mm ' .format(medida, km, cm, mm))
