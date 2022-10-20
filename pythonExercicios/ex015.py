#faça um programa que pergunte a quantidade de km percorrido por um carro alugado
# e a quantidades de dias pelo qual ele foi alugado
# calcule o preço a pagar, sabendo que a diaria é R$ 60 e cada km rodado custa R$ 0,15

km = float(input('Quantos Km foram rodados? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
total = ((km * 0.15) + (dias * 60))
print('O total a pagar é de R${:.2f}'.format(total))
