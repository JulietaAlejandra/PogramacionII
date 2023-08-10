#Muñoz Julieta Alejandra
'''d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2) que tome ambas como parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'e', 'd']'''

def listas_diferencia(lista1, lista2): 
    l1 = set(lista1)
    l2 = set(lista2)
#Los elementos en común, en orden inverso.
    comun = list(l1 & l2)
    comun.reverse()
    print(comun)
#Los elementos no comunes, en orden alfabético.
    no_comun = list(l2.symmetric_difference(l1))
    no_comun.sort()
    print(no_comun)

#Prueba...
lista1, lista2 = ['b', 'a', 'c'], ['e', 'b', 'd', 'c']
comun = []
no_comun = []

print("Listas:", lista1, lista2)
listas_diferencia(lista1,lista2)