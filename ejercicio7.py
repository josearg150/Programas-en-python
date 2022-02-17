#escribier una funcion que indique cuantas voales tiene una palabra

palabra = 'Feliz'

vocales = 0

for i in palabra:
    i = i.lower()
    vocales += 1 if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' else 0

print(vocales)