#escribir una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

from unittest import result


def calcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3 #la doble multiplicacion es elevar el numero

resultado = calcularVolumen(6)

print(resultado)