# Escreva um codigo que leia uma entrada e diga qual tipo foi digitado

palavra = input('Digite algo: ')
print('O tipo primitivo é ', type(palavra))
print('É somente espaços: ', palavra.isspace())
print('É um número; ', palavra.isnumeric())
print('É alfabetico; ', palavra.isalpha())
print('É alfanumerico; ', palavra.isnumeric())
print('Esta em maiusculas; ', palavra.isupper())
print('Esta em minuscula; ', palavra.islower())
print('Esta captalizada; ', palavra.istitle())
