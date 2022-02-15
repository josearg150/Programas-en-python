class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola soy ', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola soy el admin ', self.nombre, self.apellido, 'y soy administrador')



usuario = Usuario('Pepe', 'Feliz')
print(usuario.nombre, usuario.apellido)
usuario.saludo()
usuario.nombre = "Pancho"
usuario.saludo()
#Eliminar propiedades
#del usuario.nombre
#usuario.saludo()
#del usuario#ELiminar objeto
#print(usuario)

admin = Admin('Pepe', 'Mtz')
admin.saludo()
admin.superSaludo()