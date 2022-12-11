# Clase 53 Objetos Mutables y No Mutables

# En esta clase daremos ya una explicación definitva, de lo que es un
# objeto Mutable y No Mutable; de una forma sencilla y clara.

# En Python se indica que los siguientes tipos de datos son Inmutables:
# enteros
# float
# string
# tuplas

# Y que los siguientes datos son Mutables:
# listas
# diccionarios

# Y una de las explicaciones que hay en los foros es que si es mutable, si se puede modificar; y si no
# es mutable entonces no se puede modificar. Esto "casi" se acerca a la realidad; pero le falta el
# punto fino para que quede bien definido.

# Al escuchar lo anterior lo anterior, por lo general todos pensamoss:
# "Pero los enteros si los puedo modificar, ¿ Como es entonces que no es mutable ?"

# Un objeto es Inmutable cuando No se puede modificar su capacidad de almacenamiento en memoria y
# es Mutable cuando Si se puede modificar su capacidad de almacenamiento en Memoria. 

# A ver que quiere decir lo anterior.
# Cuando definimos un entero, un float, un string y una tupla; podemos MODIFICAR su contenido; pero
# NO su capacidad de almacenaje. Un entero siempre reservará la memoria necesaria para un Entero; ya
# esta no se puede ni AUMENTAR ni DISMINUIR. Lo mismo sucede con los float y string.

# Con las tuplas es igual; no es posible Eliminar o agregar un Elemento a una Tupla; aunque ya vimos
# en su clase correspondiente; como es posible SIMULAR esto.

# Las Listas y los Diccionarios, si son objetos mutables; porque su memoria se maneja dinámicamente; es
# decir que podemos agregar y eliminar elementos; de esta forma la reservación de la memoria CAMBIA; 
# dependiendo del número de elementos que tenga.


# Desplegamos Mensaje de la Clase
print ("Clase 53 Objetos Mutables y No Mutables")
print ()


# Define la función
def fnDespliegaUnNumero(numero):
    #Imprime los datos
	print ("Id    :",id(numero))
	print ("Valor :",numero)
	# Asignamos un nuevo valor; genera un nuevo id
	numero = 20
	print ("Id Nvo:",id(numero))
	print ("Valor :",numero)
	print ()
	numero = 30
	print ("Id Nvo:",id(numero))
	print ("Valor :",numero)
	print ()

#Creamos una varible entera
Numero = 10

#Desplegamos su id y valor
print ("Id    Fuera :",id(Numero))
print ("Valor Fuera :",Numero)
print ()

# Llamamos a la Función
fnDespliegaUnNumero(Numero)

print ("Id    Fuera despues :",id(Numero))
print ("Valor Fuera despues :",Numero)
print ()


def fnDespliegaLista(lista):
	print ("Lista Dentro Antes:",lista)
	print ("Su Id Dentro Antes:",id(lista))
	print ()
	
	# Agrega un elemento a la lista
	lista += ["Juan"]
    
	print ("Lista Despues:",lista)
	print ("Su Id Despues:",id(lista))
	print ()
    

# Definimos una lista
nombres =["Jose","Alberto","Elena"]

# Desplegamos la lista
print ("Lista Fuera Antes:",nombres)
print ("Su Id Fueta Antes:",id(nombres))
print ()

# Llamamos a la función
fnDespliegaLista(nombres)

# Desplegamos la lista
print ("Lista Fuera Despues:",nombres)
print ("Su Id Fueta Despues:",id(nombres))