# Clase 28 Listas

# En esta clase comenzaremos a ver formalmente las Estructuras de Datos que existen en Python.
# Una estrutura de datos es un objeto que almacena un COLECCIÓN de datos; que pueden ser de igual o
# diferentes tipos; y a los cuales se puede acceder de diversas formas, principalmente a través de
# un índice el cual indica su posición dentro de la estructura.

# La Estructura mas básica que hemos visto formalmente en este curso son las Cadenas o String, las
# cuales utilizan la lógica mas básica de una estructura que es la SECUENCIA. Cada caracter en la cadena
# ocupa una posición la cual la primera inicia con el Índice 0, la segunda es el índice 1; y así 
# sucesivamente.

# En esta Clase estudiaremos formalmente otra Estructura de Datos que son las Listas, la cual es la más
# versátil Estructura de Datos en Python. Esta estructura, al igual que las cadenas, permite el indexamiento,
# la partición (Slice), la Suma, la Multiplicación y la verificación de existencia de un elemento.

# La Sintaxis para crear una Lista es la siguiente
# nombre_lista = [elementos_separados_por_coma]

# Ejemplos:
# mezclados = ['Python', 'Java', 1997, 2000]
# edades    = [15, 12, 23, 14, 55 ]
# vocales   = ["a", "e", "i", "o","u"]

# Como podemos observar, los elementos de la lista pueden ser del mismo tipo o diferentes; lo cual hace 
# una característica especial de Python con respecto a Lenguajes como Java y C.

# Para acceder a los elementos de la lista, ya sea para obtener su información o para colocarla; se hace
# uso de [] y el índice de la posición del elemento que se desea obtener; o un intervalo.

# print (mezclados)        # Imprimirá todos los elementos
# print (mezclados[0])     # Imprimirá el elemento en la posición 0; Python
# edades[2] = 43           # Colocará el valor 43 en la posición 2, reemplazando el 23
# print (vocales[0:2])     # Imprimirás las 2 primeras vocales; a,e

print("Clase 28 Listas")
print()

# Declaramos 3 listas
mezclados = ['Python', 'Java', 1997, 2000]
edades    = [15, 12, 23, 14, 55 ]
vocales   = ["a","e", "i","o","u"]

#Imprimimos las 3 listas
print("Imprimiendo todos los Elementos")
print(mezclados)        # Imprimirá todos los elementos
print(edades)           # Imprimirá todos los elementos
print(vocales)          # Imprimirá todos los elementos
print()

# Imprimimos por Elementos o Subcadenas
print("Imprimiendo por Índice o Rangos")
print(mezclados[0])          # Imprimirá el elemento en la posición 0; Python
print(vocales[0:2])          # Imprimirás las 2 primeras vocales; a,e
print(vocales[0:2][1])       # Impimimos el primer elemento del Rango obnteido
print(vocales[0:4][1:3][1])  # Impimimos el primer elemento del Rango obnteido
print()

# Modificamos
print("Imprimiendo despues de Modificaciones")
edades[2] = 43           # Colocará el valor 43 en la posición 2, reemplazando el 23
print(edades)            # Imprime las Edades
#vocales[0:2]=["X"]       # Sustituye 2 valores por 1 Solo y decrementa los Elementos de la Lista
vocales[0:2]=["X","Y","Z"]         # Sustituye 2 valores por 1 Solo y decrementa los Elementos de la Lista
print(vocales)           # Imprime las vocales
edades[0:2][0]=90        # Esto no lo permite pero no marca error el Compilador
print(edades)            # Imprime las Edades
print()

# Eliminando Elementos de la Lista
print("Imprimiendo despues de Borrados")
edades.clear()                 # Elimina todos los Elementos
print("edades:",edades)        # Imprime Edades
del vocales[0]                 # Elimina la X insertada
print(vocales)                 # Imprime las vocales
del mezclados[0:2]             # Elimina por Intervalo
print(mezclados)               # Imprime Mezclados
mezclados=[]                   # Otra forma de Eliminar todos los Elementos si dejar de ser una Lista
print("mezclados:",mezclados)  # Imprime Mezclados
vocales=""                     # Otra forma de Eliminar; simplemente redefiniendo la variable
print("vocales:",vocales)      # Imprime las vocales
