# Clase 19 Sentencia if

# La instrucción if, es una sentencia que nos permite controlar el flujo del programa.
# Un programa de computadora, por lo general no tiene una secuencia lineal de ejecución; sino
# que dependiendo de diferentes circunstancias el flujo del programa cambia hacia diferentes
# direcciones.

# La Sintaxis del uso de la sentencia if es:

# if (condición) :
#    sentencias a ejecutar si SI se cumple la condición
#    sentencia 2
#    sentencia 3
# [else :]
#    sentencias a ejecutar si NO se cumple la condición
#    sdsdsdsds

# if (condición1) :
#    sentencias a ejecutar si SI se cumple la condición1
# [elif (condición2) :
#    sentencias a ejecutar si SI se cumple la condición2
# [else :]
#    sentencias a ejecutar si NO se cumple la condición1 y la condición2 
# 

print("Clase 19 Sentencia if")
print()

# Declaramos algunas variables para el Ejemplo
edad = 32
sexo = "F"
estatura =1.74

# Verifica si es mayor de edad
if (edad >= 18) :
   print("Eres mayor de Edad")
   print("Ya puedes obtener tu Credencial de Elector")

# Verifica el Sexo
if (sexo =="M") :
   print("Sexo Masculino")
   print()   
else :  
   print("Sexo Femenino")   
print

# Verifica Estatura
if (estatura > 1.75) : 
    print("Estatura Alta")
elif (estatura > 1.65) :
    print("Estatura Promedio")
else :
    print("Estatura Baja")    
