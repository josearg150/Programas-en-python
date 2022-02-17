#ingresar nombre y apellido y mostrarlos al reves

nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')

nombre = nombre + ' ' +apellido

print(nombre[::-1])