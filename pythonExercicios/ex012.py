# Faça um programa que leia o preço de um produto e aplique 5% de desconto e exiba o novo valor com desconto:

preco = float(input('Preço do produto R$ '))
n1 = preco - (preco * 5 / 100)
print(f'O valor com desconto de 5% é R${n1:.2f}')
print('O desconto foi de R${:.2f}'.format(preco * 5 / 100))
