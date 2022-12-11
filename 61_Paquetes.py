# Clase 61 Paquetes
# Paquetes, NameSpace

# En las clases anteriores, aprendimos que los Módulos nos permiten
# organizar el código; es decir que podemos ir separando el código
# de acuerdo a objetivos, funciones, etc etc etc.

# En este clase aprenderemos a utilizar los paquetes; algo muy similar
# a como funciona Java.

# En forma clara y sencilla, podemos definir que los paquetes nos sirven 
# para organizar los módulos. Asi de simple.

# Al igual que en java, los paquetes en python nos permiten organizar nuestros
# módulos a través de directorios. 

# Un paquete es un directorio que contiene archivos .py, y que adicionalmente
# debe contener un archivo de inicio llamado __init__.py. 

# En el archivo __init__.py se pueden definir declaraciones e importaciones
# de módulos; pero es posible que este archivo no contenga ninguna instrucción.
# De hecho, puede estar completamente vacío.

# A su vez, un Paquete puede contener otros paquetes. Veamos lo siguiente:

# └── paquete 
#     ├── __init__.py 
#     ├── modulo1.py 
#     └── subpaquete 
#        ├── __init__.py 
#        ├── modulo1.py 
#        └── modulo2.py

# Hay que hacer notar, que los módulos, no necesariamente tienen que pertenecer
# a un paquete, tal y como lo observamos en las clases anteriores, en donde creamos
# y usamos un módulo sin que perteneciera a paquete alguno

# Ahora para hacer uso del módulo que se encuentra en el paquete, lo hacemos
# utilizando el directorio o paquete, al cual se le otorga el nombre de
# NameSpace; seguido de un "." y posteriormente el nombre del módulo.

# Esta forma de organizar el código, impide que cuando se usen librerías de distintos
# origenes que pudieran tener funciones con el mismo nombre; al estar organizados
# en paquetes; el NameSpace impide que haya confusiones en el uso de ellas; ya que
# si 2 funciones o inclusive 2 módulos llegaran a tener el mismo nombre; no habría
# conflicto porque se encontrarían en paquetes o namespaces distintos.

# Consideraciones Importantes al Importar
# 1.- La importación de módulos debe realizarse al comienzo del documento
# 2.- En orden alfabético de paquetes y módulos.
# 3.- Primero deben importarse los módulos propios de Python. 
# 4.- Posteriormente los módulos de terceros y
# 5.- Finalmente, los módulos propios de la aplicación.
# 6.- Entre cada bloque de imports, debe dejarse una línea en blanco.

# importamos de acuerdo al paquete
#import pqFuncGrales.funcAritmeticas
from pqFuncGrales.funcAritmeticas import *


# Desplegamos Mensaje de la Clase
print ("Clase 61 Paquetes")
print ()

# Hacemos uso de las Funciones de la librería
print ("Llamando a las Funciones en el Paquete-Módulo:");
#print ("Factorial de 5:",pqFuncGrales.funcAritmeticas.factorial(5))
#print ("Cuadrado  de 5:",pqFuncGrales.funcAritmeticas.cuadrado(5))
#print ("Doble     de 5:",pqFuncGrales.funcAritmeticas.doble(5))
print ("Factorial de 5:",factorial(5))
print ("Cuadrado  de 5:",cuadrado(5))
print ("Doble     de 5:",doble(5))
input()
print ()

print ("Llamando a las Variables del Módulo:");
#print ("Sistema :",pqFuncGrales.funcAritmeticas.sistema)
#print ("Version :",pqFuncGrales.funcAritmeticas.version)
print ("Sistema :",sistema)
print ("Version :",version)

input()
print ()

# Desplegamos el nombre del módulo
print("El nombre del Modulo")
print(pqFuncGrales.funcAritmeticas.__name__)
input()
print ()
