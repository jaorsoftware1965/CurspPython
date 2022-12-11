# Clases 36

# Una Matriz, desde el punto de vista de Matemáticas es un vector que tiene
# 2 dimensiones; en donde a la primera dimensión se le conoce como Filas o
# Renglones de la Matriz; y a la segunda dimensión se le conoce como Columnas
# de la Matriz.

# En lenguajes como C y Java, definir una matriz es muy claro; porque el
# manejo de las estructuras permite indicar el número de dimensiones que
# podrá manejar un Vector.

# En Python, la implementación de una Matriz se realiza definiendo una Lista
# en la cual cada uno de sus elementos a la vez, es una Lista.

# Matriz = [[11,12,13],[21,22,23],[31,32,33],[41,42,43]]

# Para el ejemplo anterior, estamos definiendo una matriz de 4 x 3; ya que
# la Lista inicial, tiene 4 elementos los cuales se le consideran las filas
# de la Matriz; y a su vez; cada elemento es una lista de 3 Elementos; los
# cuales son considerandos las Columnas de la Matriz

# Para poder acceder a los Elementos de la Lista; se hace siguiendo la misma
# lógica que en otros lenguajes; colocando entre corchetes; el elemento que
# se desea acceder por nivel:

# print(Matriz[0][0])

# Imprimirá el elemento 11; el cual está en la Fila 0, Columna 0

# Si únicamente se coloca un Índice en la Matriz, al hacer referencia a ella,
# se estará haciendo referencia a todos los elementos de esa Fila o Renglón.

# print(Matriz[1])

# Imprimirá [31, 32, 33]

# Podemos crear Listas que cada uno de sus elementos, sean listas; y que estos
# elementos, sus Listas sean de diferentes tamaños; pero entonces ya no se 
# podrán considerar Matrices

# xMatriz = [[11,12],[22,34],[45,6,7]]
# A continuación veremos el ejemplo de como implementar tanto una Pila como una Cola.

print("Clase 36 Matrices")
print()

# Creamos una Matriz
Matriz = [[11,12,13],[21,22,23],[31,32,33],[41,42,43]]

print("Imprimiendo Elementos de la Matriz")
print(Matriz[0][0])
print(Matriz[1][2])
print(Matriz[2])
print(Matriz)
print()

# Modificando Datos
print("Modificando Matriz")
print(Matriz[0][0])
Matriz[0][0]=78
print(Matriz[0][0])
Matriz[2]=[234,245,256]
print(Matriz)
print()

#Imprimiendo Matrices
print("Imprimiendo Matrices")
for Ren in  range(len(Matriz)):
    print("Fila:",Ren)
    for Col in range(len(Matriz[Ren])):
        print(Matriz[Ren][Col],end=" ")
    print()
print()

for xList in Matriz:
    for xDato in xList:
        print(xDato,end=" ")
    print()    
print()

for xList in Matriz:
    print(xList)
    print()    


# Creando Matrices
Vector = [0] * 3
Matriz = [Vector] * 4
print("Creando Matrices")
print(Vector)
print(Matriz)
print()

# Al crear de la anterior forma el vector es el mismo 
# en las cuatro Filas
Matriz[0][0]=78
print(Matriz)
# Si modificas un vector completo, este ya es distingo
Matriz[2]=[234,245,256]
print(Matriz)
# Solo modifica los que siguen siendo el mismo
Matriz[0][0]=738
print(Matriz)
Matriz[2][1]=999
print(Matriz)
print()


# Podemos Tener lista que tenga como elementos listas con diferentes
# tamaños pero ya no se pueden considerar matrices
print("Imprimiendo No Matriz")
xNoMatriz = [[11,12],[22],[45,6,7],10]
for xList in xNoMatriz:
    if (type(xList)==list):
       for xDato in xList:
           print(xDato,end=" ")
    else:       
       print(xList)
    print()    




