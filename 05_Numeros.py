# Clase 05 Números

# En la Clase anterior, vimos que los Números en Python; pueden ser Enteros, Decimales o Complejos

# ENTEROS.
# Los números enteros son aquellos números positivos o negativos que no tienen decimales (además del cero).
# edad = 2

# Es posible indicar valores enteros en Python, aparte de Base 10; en Octal y en Hexadecimal
# num_octa = 0o71
# num_hexa = 0xff

# DECIMALES
# Los números decimales son aquellos que manejan fracciones.  Para representar un número decimal en Python
# primero se indica la Parte entera; seguida del "."; y posteriormente la fracción.
# peso = 98.750
# exponencial = 0.125e-3

# COMPLEJOS
# Los números complejos son aquellos que tienen una parte imaginaria. No es común el uso de estos Valores
# por lo que mucha gente no conoce su manejo, el cual es algo; tal y como lo dice su nombre; complejo.
# Un número complejo, consiste de un par ordenado de numeros reales en punto flotante, el cual es denotado
# como a + bj; donde a y b son los números reales y j es la parte imaginaria
# complejo = 2.1 + 7.8j

# Desplegamos Mensaje de la Clase
print("Clase 05 Números")

# Declaramos variables de tipo número 
edad = 33
edadOcta = 0o27
edadHexa = 0x20
peso = 73.50
peso2 = 9.805e1
complejo = 2.1 + 7.8j

# Imprimimos sus valores
print("edad     :",edad) 
print("edadOcta :",edadOcta) 
print("edadHexa :",edadHexa) 
print("peso     :",peso)
print("peso2    :",peso2)
print("complejo :",complejo)
print()

#Imprimos sus tipos
print("tipo de edad     :",type(edad))
print("tipo de edadOcta :",type(edadOcta))
print("tipo de edadHexa :",type(edadHexa))
print("tipo de peso     :",type(peso))
print("tipo de peso2    :",type(peso2))
print("tipo de complejo :",type(complejo))