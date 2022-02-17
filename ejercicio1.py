#multiplicar dos numeros sin usar el simbolo de la multiplicacion

numero1 = input('Ingresa el primer numero: ')
numero2 = input('Ingresa el segundo numero: ')

numero1 = int(numero1)
numero2 = int(numero2)

resultMult = 0;
for x in range(numero2):
    resultMult += numero1

print('El resultado es: ',resultMult)