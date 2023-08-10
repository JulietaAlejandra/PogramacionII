#Muñoz Julieta Alejandra

import time
from funciones import anio_bisiesto, calcular_dias_mes, calcular_edad_en_dias

nombre = input("Ingrese su nombre: ")

while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit():
        break
    else:
        print("Edad inválida. Por favor, ingrese un valor numérico.")

hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = hora_local.tm_year - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin)

print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))