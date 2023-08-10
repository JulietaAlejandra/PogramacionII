#Muñoz Julieta Alejandra
'''a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo que numero = 10: 
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 
En el programa que invoque dicha función: 
    i. El usuario debe poder ingresar el valor del parámetro numero. 
    ii. Debe validarse que el dato ingresado por el usuario corresponda a un dígito, y no a otro tipo de dato como un carácter. 
    iii. El  cálculo  debe  realizarse  utilizando  algún  tipo  de  bucle  (ej:  for, while). 
BONUS: Luego, codificar una función equivalente que utilice recursividad. '''

#iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for, while).
def suma(numero): 
    suma = 0
    for n in range(1, numero+1):
        suma = suma + n
        if n < numero:
            print(n, end= " + ")
        else:
            print(n, end= " = ")
    print(suma)

# i. El usuario debe poder ingresar el valor del parámetro numero.
while True: 
    try: # ii. Debe validarse que el dato ingresado por el usuario corresponda a un dígito 
        numero = int(input('Ingrese un numero: '))
        break
    except ValueError: #y no a otro tipo de dato como un carácter.
        print('El valor ingresado es incorrecto. Ingrese un valor numerico.')

suma(numero)