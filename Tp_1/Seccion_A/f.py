#Muñoz Julieta Alejandra
'''f. Un portal web requiere un formulario de alta de usuario donde se ingrese, mínimamente, un usuario y su correspondiente contraseña.
Escriba, en Python, una función contrasena_valida(contrasena) que devuelva True en caso de superar las siguientes validaciones sobre la
contraseña proporcionada por el usuario:
    i. Longitud entre 6 y 20 caracteres.
    ii. Debe contener al menos un número.
    iii. Debe contener al menos dos mayúsculas.
    iv. Debe contener al menos un carácter especial.
    v. No puede contener espacios.
La salida esperada es la siguiente:
    abc.123 es válida: False
    Abc.123 es válida: False
    AbC.123 es válida: True
    AbC.1 23 es válida: False
    ÁbC.123 es válida: False'''

import re
from string import *

#i.- Longitud entre 6 y 20 caracteres.
def longitud(contrasena):
    if 6 <= len(contrasena) <= 20:
        return True
    else:
        return False

#ii. Debe contener al menos un número.
def numerica(contrasena):
    if any([c.isdigit() for c in contrasena]):
        return True
    else:
        return False

#iii. Debe contener al menos dos mayúsculas.
def mayuscula(contrasena):
    if re.search('[A-Z].*[A-Z]', contrasena):
        return True
    else:
        return False

#iv. Debe contener al menos un carácter especial.
def especial(contrasena):
    if re.search('[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        return True
    else:
        return False
    
#v. No puede contener espacios.
def espacios(contrasena):
    if re.search(' ', contrasena):
        return True
    else:
        return False

#Validacion completa
def contrasena_valida(contrasena):
    if longitud(contrasena) == True and numerica(contrasena) == True and mayuscula(contrasena) == True and especial(contrasena) == True and espacios(contrasena) == False:
        return True
    else:
        return False

#Prueba...
print("abc.123", contrasena_valida("abc.123"))
print("Abc.123", contrasena_valida("Abc.123"))
print("AbC.123", contrasena_valida("AbC.123"))
print("AbC.1 23", contrasena_valida("AbC.1 23"))
print("ÁbC.123", contrasena_valida("ÁbC.123"))