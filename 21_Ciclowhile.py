# Clase 21 Ciclo while

# Un ciclo en programación, es un conjunto de instrucciones que se repiten mientras que una condición
# se cumpla.
# En Python existe la instrucción while, la cual permite ejecutar un ciclo mientras que una condición
# se esté cumpliendo

# La Sintaxis del uso de la sentencia while es la siguiente:

# while (condición) :
#    sentencias a ejecutar si SI se cumple la condición
# [else :]
#    sentencias a ejecutar si NO se cumple la condición

# Como se observa en la sintaxis, mientras que la condición se cumpla, se estarán ejecutando las sentencias
# correspondientes indicadas. Es importante mencionar que deberá de haber alguna instrucción dentro del
# bloque de sentencia ejecutadas, que provoque que un momento determinado, la condición indicada deje de
# cumplirse, porque si no fuera así; entonces el ciclo será infinito; y el programa fallaría.

# La sentencia while en Python, a diferencia de otros lenguajes; permite el uso de la palabra reservada
# else para permitir ejecutar instrucciones, si es que la condición no se cumple. 

print("Clase 21 Ciclo while")
print()

# Declaramos algunas variables para el Ejemplo
tabla = 5
multiplicador = 1

# Ciclo para desplgar la tabla de Multiplicar
while (multiplicador <= 10) :
    # Imprime la Multiplicación
    print(tabla,"X",multiplicador,"=",tabla * multiplicador)
    # Incrementa el multiplicador
    multiplicador+=1
else:
    print("Ha finalizado la impresión de la tabla")
