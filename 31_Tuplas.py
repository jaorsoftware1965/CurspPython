# Clase 31 Tuplas

# En esta Clase veremos la siguiente Estructura de Datos que es la Tupla.
# Una Tupla es una Estructura de Datos Secuencial que sirve para agrupar, como si fueran un único valor, 
# varios valores. 

# A diferencia de las Listas, las Tuplas son inmutables, es decir que no se pueden modificar una vez que
# han sido creadas; pero ya veremos en esta clase como "saltar" ese inconveniente.

# Las Tuplas utilizan los Paréntesis en lugar de los Corchetes como lo hacen las Listas.

# Para crear una Tupla, simplemente se asignan los elementos separados por coma, dentro de paréntesis.
# Ejemplo

# xTupla = ("C++","Java","Python")

# Para crear una Tupla vacía se hace de la siguiente forma.
# xTuplaVacia = ()

# Para crear una Tupla con un solo elemento, se debe de colocar el elemento seguido de una coma
# xTuplaUno =(10,)

print("Clase 31 Tuplas")
print()

# Creo 4 tuplas
xTupla = ("C++","Java","Python") # Tupla con 3 Elementos
xTuplaVacia = ()                 # Tupla Vacía
xTuplaUno = (10)                 # Esto no genera una Tupla
xTuplaOne = (10,)                # Esto genera una Tupla de 1 Elemento

# Imprimir las Tuplas
print("Imprimiendo las Tuplas")
print(xTupla)
print(xTuplaVacia)
print(xTuplaUno)
print(xTuplaOne)
print()

# Imrpimimos los Tipos
print("Imprimiendo los Tipos de Datos")
print(type(xTuplaUno))
print(type(xTuplaOne))
print()

#Imprimiendo las Longitudes
print("Imprimiendo Longitudes")
print(len(xTupla))
print(len(xTuplaVacia))
#print(len(xTuplaUno)) #Esto marca error porque no es una Tupla
print(len(xTuplaOne))
print()

print("Accediendo a sus Elementos")
print(xTupla)
print(xTupla[0])
print(xTupla[0:2])
print(xTupla[-1])
print()

print("Modificando sus Elementos")
print(xTupla)
xTupla = ("C#",)+ xTupla[1:]
print(xTupla)
print()

print("Modificando sus Elementos")
print(xTupla)
xTupla = xTupla[0:2]+("JavaScript",)
print(xTupla)
print()

print("Modificando sus Elementos")
print(xTupla)
xTupla = xTupla[0:1]+("C",)+xTupla[2:]
print(xTupla)
print()

print("Eliminando sus Elementos")
print(xTupla)
xTupla = xTupla[1:]
print(xTupla)
print()

# Defino de NUevo la Tupla
xTupla = ("C++","Java","Python") # Tupla con 3 Elementos
print(xTupla)
xTupla = xTupla[0:len(xTupla)-1]
print(xTupla)
print()

# Defino de NUevo la Tupla
xTupla = ("C++","Java","Python") # Tupla con 3 Elementos
print(xTupla)
xTupla = xTupla[0:1]+xTupla[2:]
print(xTupla)
print()