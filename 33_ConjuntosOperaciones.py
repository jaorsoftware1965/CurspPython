# Clase 33 Conjuntos Operaciones

# En esta Clase veremos otra Estructura de Datos muy particular de Python y que es
# el Conjunto.

# Un Conjunto, al igual que las Listas y las Tuplas, es una colección NO ORDENADA de
# datos, con la particularidad de que NO PERMITE ELEMENTOS REPETIDOS

# Es importante recalcar que un Conjunto es una colección NO ORDENADA de datos; 
# ya que el orden no importa, como en el caso de las Listas y Tuplas.

# Lo anterior implica que los Conjuntos, NO PERMITEN INDEXAMIENTO; es decir; que no 
# es posible acceder a sus elementos a través de un índice utilizando []

# Los Conjuntos son elementos Mutables; es decir; que se pueden modificar al igual que
# las Listas; pero sus elementos no pueden ser otras estructuras de datos.

# Para definir un Conjunto vacío se realiza de la siguiente forma:
# cVacio = set(), y no cVacio = {} como pudiera deducirse; ya que esto crearía un
# Diccionario vacío; que es una Estructura que veremos posteriormente en el curso.

# Los Conjuntos permiten las siguientes operaciones matemáticas de conjuntos:
# Unión                 expresada como a | b
# Intersección          expresada como a & b
# Diferencia            expresada como a - b
# Diferencia Simétrica  expresada como a ^ b

# A continuación veremos ejemplos de lo anteriormente expresado.

print("Clase 33 Conjuntos")
print()

# Creamos 3 conjuntos
vocales    = {"a","e","i","o","u"} # Si repetimos un elemento lo elimina
digitos    = {1,2,3,4,5,6,7,8,9,0}
digitosChr = {"1","2","3","4","5","6","7","8","9","0"}
alfabeto   = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
              "r","s","t","u","v","w","x","y","z"}

# Conjunto vacío
vacio = set()

# Imprimimos los Conjuntos
print("vocales         :",vocales)
print("vocales type    :",type(vocales))
print("digitos         :",digitos)
print("digitos type    :",type(digitos))
print("digitosChr      :",digitosChr)
print("digitosChr type :",type(digitosChr))
print("alfabeto        :",alfabeto)
print("alfabeto type   :",type(alfabeto))
print("vacio           :",vacio)
print("vacio type      :",type(vacio))
print()

# No permite Indexamiento
# print(vocales[0]) #TypeError: 'set' objects does not support indexing
# print("vocales + digitos    :",vocales + digitos) # No es permitida

print("Operaciones de Union")
print("vocales | vocales    :", vocales | vocales)
print("vocales | digitos    :", vocales | digitos)
print("vocales | alfabeto   :", vocales | alfabeto)
print("vocales | digitosChr :", vocales | digitosChr)
print("digitos | digitosChr :", digitos | digitosChr)
print()

print("Operaciones de Intersección")
print("vocales & vocales    :", vocales & vocales)
print("vocales & digitos    :", vocales & digitos)
print("vocales & alfabeto   :", vocales & alfabeto)
print("vocales & digitosChr :", vocales & digitosChr)
print("digitos & digitosChr :", digitos & digitosChr)
print()

print("Operaciones de Diferencia")
print("vocales - vocales    :", vocales - vocales)
print("vocales - digitos    :", vocales - digitos)
print("vocales - alfabeto   :", vocales - alfabeto)
print("vocales - digitosChr :", vocales - digitosChr)
print("digitos - digitosChr :", digitos - digitosChr)
print()

print("Operaciones de Diferencia Simétrica")
# Se eliminan los elementos que son comunes en ambos conjuntos
print("vocales ^ vocales    :", vocales ^ vocales)
print("vocales ^ digitos    :", vocales ^ digitos)
print("vocales ^ alfabeto   :", vocales ^ alfabeto)
print("vocales ^ digitosChr :", vocales ^ digitosChr)
print("digitos ^ digitosChr :", digitos ^ digitosChr)
print()

# Declaracion de un Conjunto utiizando Ciclo For
NumerosElevadosCuadrado = { x**2 for x in range(10) } 
print("Numeros Elevados al Cuadrado de 0-10:",NumerosElevadosCuadrado)