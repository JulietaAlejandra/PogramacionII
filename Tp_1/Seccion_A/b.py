#Muñoz Julieta Alejandra
'''b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y cuando las letras que componen dicha palabra
estén en orden alfabético, y False en caso contrario.'''

def es_abc(palabra):
    ordenado = sorted(palabra)
    return palabra == ''.join(ordenado)

#Prueba...
#Devuelve TRUE
palabra1 = "abc"
resultado1 = es_abc(palabra1)
print(resultado1)
#Devuelve FALSE
palabra2 = "abecedario"
resultado2 = es_abc(palabra2)
print(resultado2)