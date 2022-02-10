#Ddentacion
if 3 > 5:
    print('Esto no se va a imprimir')
#Los comentarios se agregan utilizando el numeral
#Comentario

#Variables
x = 5
y = 'Palabra'

#print(x, y)

email = 'ejemplo@gmail.com'

#print(email)

#multiples variables en una linea
a, b, c = 'uno', ' dos', 'tres'
#print(a, b, c)

valor1 = valor2 = valor3 = "valores"
#print(valor1, valor2, valor3)

#Concatenacion
inicio = 'Hola '
final = 'Mundo'

#print(inicio + final)

#String

palabra = 'Hola mundo'
frase = "Hola mundo comilla doble"

entero = 20 #integer
conDecimales = 20.02 # flotante
complejo = 1j #complejo

#print(palabra, frase, entero, conDecimales, complejo)

lista = [1, 2, 3]
lista2 = lista.copy()#copiar una lista en otra
lista.append(4) #Agrega datos a lista
#lista.clear()#Eliminar todos los elementos
#print(lista, lista2)
#print(lista2.count(3))#contar cuantas veces se repite el elemento
#print(len(lista))#contar todos los elementos de la lista

largolista = len(lista)
largolista2 = len(lista2)

#print(largolista, largolista2)

#print(lista[0]) #imprimir elementos de la lista

#lista.pop() #Sacar elementos de la lista
#lista.pop() #elimina al ultimo elemento de la lista
#print(lista)

#lista2.remove(1)#eliminar un elemento en especifico
#print(lista2)

lista.reverse()#invertir lista
lista.append(2)
lista.sort()#ordenar lista menor a mayor
#print(lista)

#Tuplas una vez creadas, no se modifican
tupla = ('hola', 'mundo', 'somos', 'tupla')
#print(tupla.index('hola')) #devuelve el indice donde se encuentra el elemento
listaDeTupla = list(tupla)#convertir a lista para poder modificar elementos
listaDeTupla.append('listaDeTupla')
#print(listaDeTupla)

#Rangos
rango  = range(6)
#print(rango)

#diccionarios
diccionario = {
    "nombre": "kitty",
    "raza": "Persa",
    "edad": 5
}

#print(diccionario)#imprimir todo el diccionario
#print(diccionario["nombre"])#imprimir solo el nombre
#print(diccionario.get('raza'))

diccionario['nombre'] = 'pelusa' #modificar el contenido del diccionario

#print(diccionario)
#print(len(diccionario)) #mostrar longitud del diccionario

diccionario['ronronea'] = 'Si' #agregar valores
#print(diccionario)
#diccionario.pop('ronronea') #eliminar datos del diccionario
#diccionario.popitem() #eliminar el ultimo valor agregado
#copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)
#del diccionario['ronronea']
diccionario.clear()#elminar todo del diccionario
#print(diccionario)
#print(copiaGatito)

gatitos = {
    "Fluffy":{
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba":{
        "nombre": "Black Mamba",
        "edad": 12
    }
}

gato = {
    "nombre": "pelusa",
    "edad": 7
}
gato2 = {
    "nombre": "Pantera",
    "edad": 8
}
gatos = {
    "Pelusa": gato,
    "Pantera": gato2
}
print(gatitos)
print(gatos)

perritos = dict(nombre="Rex", edad=3)
print(perritos)

#booleanos
falso = False
verdadero = True
print(falso, verdadero)