#Escribir una funcion que indique si el usuario es mayor de edad

from unittest import result


def esMayor(usuario):
    return usuario.edad > 17 #devuelve true si la edad es mayor a 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

result1 = esMayor(usuario)
result2 = esMayor(usuario2)

print(result1, result2)