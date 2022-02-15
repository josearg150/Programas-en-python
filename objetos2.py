class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo(self):
        print('Hola soy un ', self.tipo,'y mi sonido es', self.sonido)
    
#Herencia
class Gato(Animal):
    tipo = 'gato'
    #Extendiendo el comportamiento de def
    def __init__(self, nombre, sonido):
        Animal.__init__(self, nombre, sonido)
        print('hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
        print('Instanciando un perro')

class Pato(Animal):
    tipo = 'pato'

gato = Gato('Pelusa', 'miau')
perro = Perro('Rex', 'Guau')
pato = Pato('Zapatop','cuack')
gato.saludo()
perro.saludo()
pato.saludo()