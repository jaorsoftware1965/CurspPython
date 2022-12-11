# Clase 57 Modulos

# Un módulo, dicho de la forma mas sencilla posible, es un
# archivo que contiene código python; que pueden ser declaraciones
# funciones, etc etc.

#importamos nuestras funciones
import funcAritmeticas

# Desplegamos Mensaje de la Clase
print ("Clase 57 Módulos")
print ()

# Hacemos uso de las Funciones de la librería
print ("Llamando a las Funciones en el Módulo:");
print ("Factorial de 5:",funcAritmeticas.factorial(5))
print ("Cuadrado  de 5:",funcAritmeticas.cuadrado(5))
print ("Doble     de 5:",funcAritmeticas.doble(5))
input()
print ()

print ("Llamando a las Variables del Módulo:");
print ("Sistema :",funcAritmeticas.sistema)
print ("Version :",funcAritmeticas.version)
input()
print ()

# Desplegando la información del Módulo
print (dir(funcAritmeticas))
print ("Variable __name__        :",funcAritmeticas.__name__)
print ("Variable __loader__      :",funcAritmeticas.__loader__)
print ("Variable __package__     :",funcAritmeticas.__package__)
print ("Variable __spec__        :",funcAritmeticas.__spec__)
print ("Variable __spec__.origin :",funcAritmeticas.__spec__.origin)
input()
print ()

# Importando librerías de python
import sys
print (dir(sys))
input ()

# Desplegando información de las variables de la librería importada
print ("Variable version        :",sys.version)
print ("Variable version_info   :",sys.version_info)
print ("Variable winver         :",sys.winver)
print ("Variable path           :",sys.path)



