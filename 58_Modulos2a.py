# Clase 58 Modulos2a

# En esta clase veremos como importar funciones específicas
# de una librería para tenerlas disponibles, directamente y
# no tener que colocar el prefijo del nombre de la librería para
# poder utilizarlas


#importamos funciones específicas
from funcAritmeticas import factorial
from funcAritmeticas import cuadrado
from funcAritmeticas import doble
from funcAritmeticas import sistema
from funcAritmeticas import version
from funcAritmeticas import *


# Desplegamos Mensaje de la Clase
print ("Clase 58 Módulos2a")
print ()

# Hacemos uso de las Funciones de la librería
print ("Llamando a las Funciones en el Módulo:");
print ("Factorial de 5:",factorial(5))
print ("Cuadrado  de 5:",cuadrado(5))
print ("Doble     de 5:",doble(5))
input()
print ()

print ("Llamando a las Variables del Módulo:");
print ("Sistema :",sistema)
print ("Version :",version)
input()