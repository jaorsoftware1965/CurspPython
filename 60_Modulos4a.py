# Clase 60 Modulos4a

# Existen varios módulos de python, como son time, math y sys que ya se encuentran
# incorporados, por razones de velocidad, en el Interprete de Python, los cuales
# están escritos en C. A wiwi !

# Estas funciones seguramente se encontrarán en algun archivo .lib, dll, o .a
# Para saber cuales son las librerías que ya vienen incorporadas en el interprete
# hacemos uso de la librería sys; y desplegamos el objeto builtin_module_names

# importamos la librería sys
import sys

# desplegamos los nombres de las librerias que están incluidas en python
print (sys.builtin_module_names)
input()

#importamos la libreria time
import time

# desplegamos su documentacion
print (dir(time))
input()

print (time.__doc__)
input()
