#encontrar el menor numero de una lista

from mimetypes import init


lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for i in lista:
    if( menor == 'init'):
        menor = i
    else:
        menor = i if i < menor else menor

print('Menor: ',menor)