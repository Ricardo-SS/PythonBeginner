# programa que leia um número inteiro e mostre sua taboada

n = int(input('Didgite um numero: '))
print('Taboada de: ',n)
print('-' * 10)
a1 = n * 1
a2 = n * 2
a3 = n * 3
a4 = n * 4
a5 = n * 5
a6 = n * 6
a7 = n * 7
a8 = n * 8
a9 = n * 9
print('\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}'.format(n,a1,n,a2,n,a3,n,a4,n,a5,n,a6,n,a7,n,a8,n,a9))
print('-' * 10)

"""
# A forma com foi feita anteriormente funciona porem poderia ter sido escrito de uma forma melhor. veja o exemplo abaixo
# Porem com o conhecimento que temos ate agora a primeira forma é mais adequanda.
num = int(input('Didgite um numero: '))
i = int(1)
print('Taboada de: ',num)
print('-' * 14)
while (i < 10):
    print(num, " x ", i, " = ", num * i)
    i +=1
print('-' * 14)
print("Fim da taboada")
"""