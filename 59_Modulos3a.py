# Clase 59 Modulos3a

# En esta clase aprenderemos como es que python controla la 
# importación de archivos.

# En nuestra clase anterior, el archivo con nuestro código
# se encuentra en nuestro mismo directorio del programa principal.

# Pero como es que python encuentra sys.py si no está en el directorio?

# A la hora de importar un módulo Python recorre todos los directorios 
# indicados en la variable de entorno PYTHONPATH en busca de un archivo 
# con el nombre adecuado. El valor de la variable PYTHONPATH se puede 
# consultar desde Python mediante sys.path

# De esta forma para que nuestro módulo estuviera disponible para todos 
# los programas del sistema bastaría con que lo copiáramos a uno de los 
# directorios indicados en PYTHONPATH.

# En el caso de que Python no encontrara ningún módulo con el nombre especificado, 
# se lanzaría una excepción de tipo ImportError.


#importamos funciones específicas
#from funcAritmeticas import factorial
#from funcAritmeticas import cuadrado
#from funcAritmeticas import doble
#from funcAritmeticas import sistema
#from funcAritmeticas import version
from funcAritmeticas import *


# Desplegamos Mensaje de la Clase
print ("Clase 59 Módulos3a")
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

import sys
print(sys.path)