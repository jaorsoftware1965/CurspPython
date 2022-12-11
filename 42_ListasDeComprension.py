# Clase 42 Listas de Comprensión

# En esta clase veremos una característica muy particular y singular de Python que son
# las listas de Comprensión.

# Una Lista de Comprensión es un forma ágil y reducida de crear una lista utilizando
# expresiones muy particulares.

# Es un tipo de instrucción, delimitada por corchetes, que consta de una expresión 
# seguida de una o varias claúsulas for y opcionalmente, una o varias clausulas if, 

# Desplegamos Mensaje de la Clase
print("Clase 42 Listas de Comprensión")
print()

# Suponga que se tiene la siguiente lista
nombres = ['Juan','Josefina','Alberto',"Marcos"]

# Y pretendemos imprimir los nombres en mayúsculas
# Si lo hicieramos con un ciclo for sería así

# Ciclo para acceder a cada una de las letras por indice
print ("Imprimiendo Nombres en Mayúsculas con un Ciclo Normal")
for xNombre in nombres :
    print (xNombre.upper())
print ()


# Utilizando listas de Comprensión, lo anterior que daría así:
print ("Imprimiendo Nombres en Mayúsculas con Lista de Comprensión")
[print (xNombre.upper()) for xNombre in nombres]
print ()

# La lista original intacta
print ("Lista original intacta")
print (nombres)
print ()

# El ejemplo anterior imprime los nombres en mayúsculas pero no modifica la
# Lista original.
# Si quisieramos modificar la lista original con un ciclo for, sería

# Ciclo para modificar la lista
for Indice in range(len(nombres)):
    nombres[Indice] = nombres[Indice].upper()
print ("Lista Original Modificada con Ciclo For")    
print (nombres)
print ()

# Si lo hicieramos con listas de Comprensión
nombres = ['Juan','Josefina','Alberto',"Marcos"]
print ("Lista Original")    
print (nombres)
print ()

nombres = [xNombre.upper() for xNombre in nombres]
print ("Lista Original Modificada con Lista de Comprensión")    
print (nombres)
print ()

# Veamos otro ejemplo
numeros = [1,2,3,4,5,6,7,8,9,10]

# Obtengamos una lista de los elementos multiplados por 3
alTriple = [xNum * 3 for xNum in numeros]
print ("Lista de Numeros al Triple")
print (alTriple)
print ()

# Ahora obtenemos una lista de números pares
pares = [xNum for xNum in numeros if xNum % 2 == 0]
print ("Lista de Numeros Pares")
print (pares)
print()

# Aplicando una función 
lenNombres  = [len(xNombre) for xNombre in nombres]
print ("Longitud de cada nombre")
print (nombres)
print (lenNombres)
print ()

# Ahora obtendremos una tupla
listaDeTuplas = [(xNombre,len(xNombre)) for xNombre in nombres]
print ("Imprimiendo la Tupla Generada")
print (listaDeTuplas)
print (type(listaDeTuplas))
