# Clase 04 Variables y Tipos de Datos

# Una variable es un un espacio de memoria en el cual se almacena información y a la cual se le
# le asigna un Identificador o nombre, para poder manipular la información.

# Las Variables en Python, manejan 3 tipos de Datos Básicos iniciales que son:

# Números. Cualquier valor numérico; entero, decimal o complejo
# Cadenas. Conjunto de 1 o mas caracteres, los cuales se encuentran delimitados por "s 0 's.
# Booleanos. Solo pueden tomar el valor de True o False

# En Python, para declarar una variable; no es necesario indicar su Tipo; el Compilador sabe
# identificarlo, de acuerdo al valor que se le asigne.
# Para crear una variable simplemente se sigue la siguiente sintaxis:
# 
# identificador = valor
# 
# La anterior instrucción creará un variable con el identificador escrito y le asignara el valor
# indicado. De acuerdo a este valor, el compilador sabe de que tipo es la variable.

# Python permite la asignación multiple de las siguientes formas:

# a = b = c = 1
# a,b,c = 1,2,"jaor"

# En la primera instrucción creará las variables a,b,c; las 3 con el valor de 1
# En la segunda instrucción crear la variable a=1, b=2 y c="jaor"

# Python nos proporciona la función type la cual nos permite conocer el tipo de dato de una variable
# En Python una variable puede cambiar de un tipo de dato a otro, simplemente cambiando su valor

# Desplegamos Mensaje de la Clase
print("Clase 04 Variables y Tipos de Datos Base")

# Declaramos variables y las imprimimos
a=b=c=1
print("a:",a)
print("b:",b) 
print("c:",c)
print()

# Cambiamos su valores 
a,b,c=  10,True, "jaor"
print("a:",a); 
print("b:",b); 
print("c:",c)
print()

#Imprimos sus tipos
print("tipo de a:",type(a))
print("tipo de b:",type(b))
print("tipo de c:",type(c))

print(a.bit_length)