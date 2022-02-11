#if
if 2 < 5:
    print('2 es menor que 5')

if 2 == 2:
    print('2 es igual a 2')

if 2 == 3:
    print('2 es igual a 3')

if 2 > 5: 
    print('2 es mayor a 5')

if 2 != 2:
    print('2 diferente de 2')

if 3 >= 2:
    print ('3 es mayor a 2')

if 2 <= 2:
    print('2 es menor o igual a 2')

if 2 > 1:
    print('lala')
elif 2 < 4:
    print('2 es menor a 4 en elif')
else:
    print("yo me imprimo solo si todo lo anterior evalua en falso")
#operador ternario
print('Cuando devuelve true') if 5 > 2 else print('Cuando devuelve false')

#and y or 
if 2 < 5 and 4 > 3:
    print('Todo es verdadero')

if 1 < 0 or 1 > 0:
    print('Una de las condiciones devolvio true')