#Muñoz Julieta Alejandra
'''a. Escribir una función de nombre palabra_no_tiene_letras(palabra, letras_prohibidas),
la cual retorne True si es que los caracteres que componen una palabra no se encuentran en una lista de caracteres prohibidos.'''

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            #Tiene letras prohibidas
            return False
    #No tiene letras prohibidas
    return True

#Prueba...
#Deveulve FALSE
palabra = "perro"
letras_prohibidas = ["a", "e", "i", "o", "u"]
resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
print(resultado)
#Devuelve TRUE
palabra = "mariposa"
letras_prohibidas = ["d", "f", "g", "h", "z"]
resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
print(resultado)