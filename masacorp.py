# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
# e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
# IMC = peso (kg)/ [estatura (m)]2
# import math
# v = 2.357
# print(math.ceil(v*100)/100)  # -> 2.36
# print(math.floor(v*100)/100)  # -> 2.35

import math
peso = 70
altura = 1.74

frase = "Tu índice de masa corporal es "
indice = peso / altura ** 2
indice = str(math.floor(indice*100)/100)
print(frase + indice)
