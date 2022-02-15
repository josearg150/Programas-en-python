#c = open('texto.txt', 'w') #r permiso de leer, a agregar mas texto, w para modifcar, x para crear
#print(c.readline())
#print(c.readline())
#print(c.readline())

#for linea in c:
#    print(linea)

#c.write('\nAgregando una linea al archivo')

#c.close()

#x = open('texto.txt')
#print(x.read())
#Eliminar archivo
import os 
if os.path.exists('texto.txt'):
    os.remove('texto.txt')
else: 
    print('El archivo no existe')