#crie um programa que lei o nome de quatro alunos e sortei um deles para apagar o quadro e mostre o nome na tela:
from random import choice
n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}!')