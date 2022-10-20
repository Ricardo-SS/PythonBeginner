# criar um prograa que leia quantos reais tem na carteira e quantos dolares da pra comprar.

real = float(input('Quanto dinheiro você tem? R$ '))
dolla = real / 5.40
print(f'Com R${real:.2f} você pode comprar U$${dolla:.2f}')
