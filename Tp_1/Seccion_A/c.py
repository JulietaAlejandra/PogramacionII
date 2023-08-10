#Muñoz Julieta Alejandra
'''c. Escriba un procedimiento procesar_palabras(entrada) que acepte una secuencia de palabras separadas por coma,las ordene y las imprima.
Suponiendo que la entrada provista al programa es la siguiente: te,felicito,que,bien,actuas
La salida esperada es: actuas,bien,felicito,que,te'''

def procesar_palabras(entrada):
    palabras = entrada.split(",") #Convierte/agrega la entrada a una lista
    palabras.sort() #Ordena la lista
    print(','.join(palabras)) #Devuelve un str

#Prueba...
entrada = str(input("A continuacion, ingrese palabras separadas por coma: "))
procesar_palabras(entrada)