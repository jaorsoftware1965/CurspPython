# Clase 32 Tuplas Operaciones Indexamiento Slice Funciones

# Al igual que las Listas, las Tuplas permiten Indexamiento (desde 0), concatenación, multiplicación
# y Pertenencia.

# Las Tuplas tambien utilizan los operadores + y * como las Cadenas y las Listas; solo que en este caso
# el resultado de la operación es una Tupla.

# A continuación la tabla que muestra estas operaciones

# ----------------------------------------------------------------------------------------------------
#   Expresión                   Resultado                           Operación/Descripción
# ----------------------------------------------------------------------------------------------------
#   (1, 2, 3) + (4, 5, 6)	    (1, 2, 3, 4, 5, 6)	                Concatenation
#   ('abc',) * 4	            ('abc', 'abc', 'abc', 'abc')	    Repetition
#   13 in (13, 32, 43)	        True	                            Pertenencia

#   Sea T=('C++', 'Java', 'Python')
#   T[2]	                    'Python'	                        Por Posición
#   T[-2]	                    'Java'	                            Negativo contando desde la Derecha
#   T[1:]	                    ('Java', 'Python')	                Por rango

# Las siguiente Funciones están disponibles para las Tuplas y las veremos funcionando ya directamente
# en el código

print("Clase 32 Tuplas Operaciones Indexamiento Slice Funciones")
print()

# Declaramos una tupla
xTupla = ("C++","Python","Java","C")

# Imprime la Tupla
print("count C++:",xTupla.count("C++"))
print("index C  :",xTupla.index("C"))
print("max:",max(xTupla))
print("min:",min(xTupla))
print()

# Declara una Lista
list1= ['Html', 'CSS', 'JavaScript', 'Php']
xTupla = tuple(list1)
print ("Tupla desde Lista : ",xTupla)

# Declara una Cadena
sCadena = "JaorSoftware"
xTupla = tuple(sCadena)
print ("Tupla desde Cadena : ", xTupla)

