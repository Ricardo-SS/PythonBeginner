"""criar um programa que leia o nome completo de uma pessoal e mostre na tela ele
   todo em maiusculo, minusculo, quantas letras tem sem espaços
   e quantas letras tem o primeiro nome"""

#primeira maneira
"""nome = str(input('Nome completo: '))
nome1 = nome.strip()        #remove os espaços iniciais e finais se houver
nome2 = nome1.split()       #separa cada nome como um estring, em listas
novonome = ''.join(nome2)   #junta todos nomes
print(nome.upper())         #coloca tudo em MAIÚSCULAS
print(nome.lower())         #coloca tudo em minusculas
print('O primeiro nome tem {} letras;'.format(len(nome2[0])))
print('O nome completo tem um total de {} letras!'.format(len(novonome)))"""

#Segunda maneira
"""nome = str(input('Digite o nome completo: ')).strip()   #recebe o nome digitado ja sem os espaços iniciais e finais por conta do strip
print('Nome em Maiúsculas: {}'.format(nome.upper()))    #coloca todas as letras em maiusculas
print('Nome em Minúsculas: {}'.format(nome.lower()))    #coloca todas as letras em minusculas
nome = nome.split()                                     #cria uma lista separada para cada nome
print('O primeiro nome tem um total de {}'.format(len(nome[0])))            #contas as letras da lista 0
print('O nome completo tem um total de {}'.format(len(''.join(nome))))      #contas as letras de todas as listas"""

#terceira maneiras
nome = str(input('Digite o nome completo: ')).strip()
print('Nome em Maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('O nome completo tem um total de {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem um total de {} letras'.format(nome.find(' ')))
