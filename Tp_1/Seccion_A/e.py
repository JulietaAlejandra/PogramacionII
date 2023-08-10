#Muñoz Julieta Alejandra
'''e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista e imprima ambas. La lista de números la ingresa el usuario en forma de números separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81'''

def numeros_par_impar(entrada):
    numeros = [int(num) for num in entrada.split(",")]
    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num ** 2)

    print(','.join(map(str, pares)))
    print(','.join(map(str, impares)))

#Prueba...
entrada_usuario = input("Ingrese la lista de números separados por comas: ")
numeros_par_impar(entrada_usuario)