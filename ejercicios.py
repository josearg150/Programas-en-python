#dato = input('Ingrese dato: ')

#lista = ('hola', 'mundo', 'feliz', 'dragon')

#if lista.count(dato) > 0:
  #  print('El dato existe: ',dato)
#else:
 #   print('El dato no existe: ',dato)

from ast import expr_context


primero = input('Ingrese el primer numero: ')
#validacion para strings 
try:
    primero = int(primero)
except:
    primero = 'hola'

if primero == 'hola':
    print('El valor ingresado no es un entero')
    exit()#Terminar el programa

segundo = input('Ingrese el segundo numero: ')
#validacion para strings
try:
    segundo = int(segundo)
except:
    segundo = 'hola'

if segundo == 'hola':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese una operacion: ')

if simbolo == '+':
    print('Suma: ',primero + segundo)
elif simbolo == '-':
    print('Resta: ',primero - segundo)
elif simbolo == '*':
    print('Multiplicacion: ',primero * segundo)
elif simbolo == '/':
    print('Division: ',primero / segundo)
else:
    print('Simbolo invalido')
