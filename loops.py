#i = 0

#while i < 5:
#    i += 1
#    if i == 3:
#        continue #break
#    print(i)

#usuarios= ['Hola', 'Jose', 'Roberto']

#for usuario in usuarios:
#    print(usuario)

#usuario = 'Jose'

#for c in usuario:
#    print(c)

#usuarios= ['Hola', 'Jose', 'Roberto']

#for usuario in usuarios:
#    if usuario == 'Jose':
#        break
#    print(usuario)

#for x in range(3, 30, 3): #el tercer elemento es el aumento de la iteracion
#    print(x)
#else:
    #print('Hemos terminado')

#usuarios= ['Hola', 'Jose', 'Roberto']

#edades = [24, 25, 26]

#for usuario in usuarios:
#    for edad in edades:
#        print(usuario, edad)

def miFuncion():
    print('Mi primera funcion en python')

#miFuncion()

def imprimeDato(*nombre):
    print('Mi argumento es', nombre[1])

#imprimeDato('Hola', 'Jose', 'Roberto')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre = 'Jose', apellido = 'Garcia')

def nombrecompleto2(**kwargs): #key arguments
    print(kwargs['nombre'], kwargs['apellido'])

#nombrecompleto2(nombre = 'Jose', apellido = 'Feliz')

def concatenaNombre(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenaNombre(['Jose', 'Garcia'])

#print(nombres)

def recursion(i):
    if ( i < 1 ):
        return i
    print(i)
    recursion(i - 1)

recursion(6)