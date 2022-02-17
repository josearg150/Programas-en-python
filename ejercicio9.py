#funcion que recibe nombre y apellido y los agrega a un archivo

def agregaArchivo(nombre, apellido):
    c = open('listaNombres.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaArchivo('Jose', 'Rocha')