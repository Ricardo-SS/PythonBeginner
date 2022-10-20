#criar um programa que receba o nome de 4 alunos e sortei uma orde de apresentaçao, e mostre essa ordem na tela

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A orde de apresentação é {lista}')