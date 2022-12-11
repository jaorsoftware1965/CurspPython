# Clase 45 Funciones

# Uno de los aspectos fundamentales en cualquier lenguaje de Programación, son las Funciones. Esta
# característica es una de las bases principales para que un lenguaje sea modular; es decir; que trabaje
# a base de módulos; los cuales pueden estar separados y que tienen la capacidad de  ser distribuidos y 
# usados en diferentes partes de un sistema.

# Las Funciones permiten evitar la redundancia de código; ya que cuando un código es claramente visible
# que se repite una y otra vez; entonces debe ser convertido en una función; para que solo sea escrito
# una sola vez.

# Unna Función es un bloque de código, al cual se le asigna un nombre; y este nombre es el que se utiliza
# para ejecutarlo.

# Python provee al programador de un conjunto de instrucciones para diversos objetivos, las cuales hemos
# estado ya utilizando; como por ejemplo la función print.

# Python y cualquier otro lenguaje de programación provee la capacidad para crear nuestras propias funciones
# las cuales son llamadas "Funciones de Usuario."

# Para definir una función en Python, usa la siguiente sintaxis:

# def functionname ( [parameters] ):
#     ["function_docstring"]
#     sentences
#     [return] [expression]
 
# Como se observa se utiliza la palabra reservada def seguido del nombre de la función
# Despues se utilizan paréntesis para inidicar parámetros los cuales son opcionales
# Opcionalmente se puede utilizar una cadena de texto para explicar lo que hace la función
# Sentenncias que se ejecutarán
# Finalmente se utiliza la palabra reservada return la cual puede ser seguida de un valor a retornar

# Una vez que la función se encuentra definida, es posible llamarla desde cualquier parte del programa
# las veces que sea necesario.

# Las funciones deben de respetar la regla de indentación que se utiliza en los bloques como hemos
# visto anteriormente y deben estar definidas antes de ser llamadas.


# Desplegamos Mensaje de la Clase
print ("Clase 45 Funciones")
print ()

# Definimos una función para imprimir un mensaje
def fnInfoSistema():
   "Imprime información del Sistema"
   print ("SV Ver 1.0")
   return
   

# Se llama a la función
fnInfoSistema()
fnInfoSistema()
fnInfoSistema # No ejecuta nada


# NameError: name "verSistema" is not defined



def fnStrVerSistema():
   "Devuelve la Versión del Sistema"
   return ("Ver 1.0")


# Se llama a la función
print (fnStrVerSistema())
print (fnStrVerSistema())

# Colocamos el valor retornado en una variable
version = fnStrVerSistema()

# Imprimimos la variable
print ("La versión es:",version)

# El tipod de dato
print (type(version))


fnStrVerSistema()