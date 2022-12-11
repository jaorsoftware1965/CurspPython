# Clase 63 Paquetes 3a

# Especificando en el módulo que funciones y variables están disponibles
# al realizar un import utilizando from

# importamos de acuerdo al paquete
from pqFuncGrales.funcAritmeticas import *
import pqFuncGrales.funcAritmeticas

# Desplegamos Mensaje de la Clase
print ("Clase 63 Paquetes 3a __all__")
print ()

# Hacemos uso de las Funciones de la librería
print ("Llamando a las Funciones en el Paquete-Módulo:");
#print ("Factorial de 5:",factorial(5))
#print ("Cuadrado  de 5:",cuadrado(5))
#print ("Doble     de 5:",doble(5))
print ("Factorial de 5:",pqFuncGrales.funcAritmeticas.factorial(5))
print ("Cuadrado  de 5:",pqFuncGrales.funcAritmeticas.cuadrado(5))
print ("Doble     de 5:",pqFuncGrales.funcAritmeticas.doble(5))
input()
print ()

print ("Llamando a las Variables del Módulo:");
#print ("Sistema :",sistema)
#print ("Version :",version)
print ("Sistema :",pqFuncGrales.funcAritmeticas.sistema)
print ("Version :",pqFuncGrales.funcAritmeticas.version)
input()
print ()
print (dir(pqFuncGrales.funcAritmeticas))
