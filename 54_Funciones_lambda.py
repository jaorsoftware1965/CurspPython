# Clase 54 Funciones Lambda

# En esta clase veremos un tema mas con respecto a funciones
# que en python es conocido como Funciones Anónimas o
# funciones lambda

# La sintaxis para crear una función lambda es:

# nombre_funcion = lambda [lista_parametros]:expresion_devolver

# donde:
# expresion_devolver no debe tener múltiples lineas


# Desplegamos Mensaje de la Clase
print ("Clase 54 Funciones Lambda")
print ()

# Definimos la función lambda multiplica
multiplica = lambda numero1, numero2: numero1 * numero2

print ("Usamos la función cuadrado")
print (multiplica(5,8))

# Definimos la función lambda multiplica
multiplica2 = lambda numero1, numero2=5: numero1 * numero2

print ("Usamos la función cuadrado2")
print (multiplica2(5))
