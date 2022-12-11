# Clase 25 Funciones para Números

# Así como hemos visto que hay funciones para las Cadenas, tambien existen funciones para los valores
# numéricos y a continuación veremos cada una de ellas.

# Para hacer uso de estas funciones, deberemos de importar el Módulo "math", el cual contiene la definición
# de la mayoría de estas funciones.

# Importamos el Módulo 
import math

# Mensaje de impresión
print("Clase 25 Funciones de Números")
print("-----------------------------")
print()

#El valor de pi
print("El valor de pi:",math.pi)
print()

# Valor absoluto
print("abs(-45)    : ", abs(-45))
print("abs(100.12) : ", abs(100.12))
print()

print("math.fabs(-45.17) : ", math.fabs(-45.17))
print("math.fabs(100.12) : ", math.fabs(100.12))
print()

#Redondea al número mayor entero siguiente
print("math.ceil(100.12)  : ", math.ceil(100.12))
print("math.ceil(100.72)  : ", math.ceil(100.72))
print("math.ceil(-45.17)  : ", math.ceil(-45.17))
print("math.ceil(math.pi) : ", math.ceil(math.pi))
print()

# Redondea al número menor entero siguiente
print("math.floor(100.12)  : ", math.floor(100.12))
print("math.floor(100.72)  : ", math.floor(100.72))
print("math.floor(-45.17)  : ", math.floor(-45.17))
print("math.floor(math.pi) : ", math.floor(math.pi))
print()

# El valor máximo
print("max(80, 100, 1000) : ", max(80, 100, 1000))
print("max(-20, 100, 400) : ", max(-20, 100, 400))
print("max(-80, -20, -10) : ", max(-80, -20, -10))
print("max(0, 100, -400) : ", max(0, 100, -400))
print()

# El valor mínimo
print("min(80, 100, 1000) : ", min(80, 100, 1000))
print("min(-20, 100, 400) : ", min(-20, 100, 400))
print("min(-80, -20, -10) : ", min(-80, -20, -10))
print("min(0, 100, -400) : ", min(0, 100, -400))
print()

# Elevar a la potencia
print("math.pow(10, 3) : ", math.pow(10, 3))
print("math.pow(10, -2) : ", math.pow(10, -2))
print("math.pow(5, 4) : ", math.pow(5, 4))
print("math.pow(7, 0) : ", math.pow(7, 0))
print()

# Redondear a un número de decimales
print("round(80.23456) : ", round(80.23456))
print("round(80.23456) : ", round(80.53456))
print("round(100.000056, 3) : ", round(100.0576, 3))
print("round(100.000056, 3) : ", round(100.05651, 3))
print("round(-100.000056, 3) : ", round(-100.0576, 3))
print("round(-100.000056, 3) : ", round(-100.0565, 3))
print()

# Raiz Cuadrada 
print("math.sqrt(100) : ", math.sqrt(100))
print("math.sqrt(7) : ", math.sqrt(7))
print("math.sqrt(math.pi) : ", math.sqrt(math.pi))
print()
