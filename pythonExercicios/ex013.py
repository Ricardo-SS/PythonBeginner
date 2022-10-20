# crie um programa que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento:
sal = float(input('Digite valor do salário: '))
nsal = sal + (sal * 15 / 100)
print('O novo salário é R${:.2f}'.format(nsal))
