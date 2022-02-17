#Escribir una aplicacion que reciba una cantidad infinita de numeros hasta
#decir basta, luego que devuelva la suma de los numeros ingresador

lista = []
print('Ingresa numoers y para salir escribe "basta"')
while True:
    valor = input('Ingresa un valor: ')
    if valor == 'basta':
        break;
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('El dato ingresado no es valido')
            exit()

suma = 0
for i in lista:
    suma += i

print('La suma es: ',suma)
