#Muñoz Julieta Alejandra
'''c. Tal como sucede con la lógica proposicional, en Python muchas veces las expresiones booleanas pueden ser simplificadas manteniendo el valor de 
verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente a a and b. A continuación, intente simplificar las siguientes expresiones y 
escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el valor de verdad de las expresiones ya simplificadas: 
    i. (a or b) or (b and c) 
    ii. b and c or False 
    iii. a and b or c or (b and a) 
    iv. a == True or b == False '''

def procesar_sentencias(a, b, c):
    expresion1 = a or b or (b and c)
    expresion2 = b and c or False
    expresion3 = a and b or c or (b and a)
    expresion4 = a == True or b == False
    
    print(f"Expresión 1: {expresion1}")
    print(f"Expresión 2: {expresion2}")
    print(f"Expresión 3: {expresion3}")
    print(f"Expresión 4: {expresion4}")

#Prueba
a = True
b = False
c = True

procesar_sentencias(a, b, c)