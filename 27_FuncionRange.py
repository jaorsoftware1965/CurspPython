# Clase 27 función range

# En clases anterior hemos utilizado la función range, pero sin tener una explicación a fondo de ella.
# En esta clase veremos formalmente el uso de la función, ya que su uso es muy común e importante, y es
# necesario tener un conocimiento a fondo de su funcionamiento.
# 
# La sintaxis de uso de la función range es la siguiente:
# 
# range(stop) 
# range(start, stop[, step]) 
# 
# Como podemos observar, tiene 2 formas de utlizarse; con tan solo un argumento; o con 2 argumentos,
# teniendo un tercero como opcional

# A continuación consideraciones que hay que tener al usar la función range
# Los argumentos de la función deben ser valores ENTEROS.
# Si el argumento step es onitido, su valor por default es 1
# Si el argumento start es omitido,su valor por default es 0
# Para valores positivos en el argumento step, el rango de valores se calcula de la siguiente forma:
#      r[i] = start + step * i; donde i>=0 y r[i] < stop
#      r[0] =    3  +  1   * 0 = 3
#      r[1] =    3  +  1   * 1 = 4
#      r[2] =    3  +  1   * 2 = 5
#      ......
#      r[6] =    3  +  6   * 1 = 9

# Para valores negativos en el argumento step, el rango de valores se calcula de la siguiente forma:
#      r[i] = start + step * i; donde i>=0 y r[i] > stop
#      r[0] = -5    +  -1  * 0; = -5
#      r[1] = -5    +  -1  * 1; = -6
#      r[2] = -5    +  -1  * 2; = -7
#      ......
#      r[7] = -5    +  -1  * 7; = -12


print ("Ejemplos con steps de 1 y -1")
print ("range (10)         :",list(range(10)))
print ("range (-10)         :",list(range(-10)))
print ("range (3,10)       :",list(range(3,10)))
print ("range (1,11)       :",list(range(1,11)))
print ("range (5,11)       :",list(range(5,11)))
print ("range (-5,3)       :",list(range(-5,3)))
print ("range (-5,-3)      :",list(range(-5,-3)))
print ("range (-5,-13)     :",list(range(-5,-13)))
print ("range (-5,-13,-1)  :",list(range(-5,-13,-1)))
print ("range (10,0,-1)    :",list(range(10,0,-1)))
print ()

print ("Ejemplos con steps de 2 y -2")
print ("range (10,2)       :",list(range(10,2)))
print ("range (2,10,2)     :",list(range(2,10,2)))
print ("range (3,10,2)     :",list(range(3,10,2)))
print ("range (1,11,2)     :",list(range(1,11,2)))
print ("range (5,11,2)     :",list(range(5,11,2)))
print ("range (-5,3,2)     :",list(range(-5,3,2)))
print ("range (-5,-3,2)    :",list(range(-5,-3,2)))
print ("range (-5,-13,2)   :",list(range(-5,-13,2)))
print ("range (-5,-13,-2)  :",list(range(-5,-13,-2)))
print ("range (10,0,-2)    :",list(range(10,0,-2)))

