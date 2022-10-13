# Escreva um codigo que leia uma entrada e diga qual tipo foi digitado

elemento = input("Digite algo: ")
print("O tipo primitivo é __: ", type(elemento))
print("É somente espaços____: ", elemento.isspace())
print("É um numerio_________: ", elemento.isnumeric())
print("É alfabetico_________: ", elemento.isalpha())
print("É alfanumerico_______: ", elemento.isnumeric())
print("Esta em maiusculo____: ", elemento.isupper())
print("Esta em minusculo____: ", elemento.islower())
print("Está captalizada_____: ", elemento.istitle())
