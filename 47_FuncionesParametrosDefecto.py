# Clase 47 Funciones Parámetros por Defecto y Orden

# Otro aspecto importante a considerar en Funciones, es que cuando definimos 2 con el mismo nombre, 
# Python no marca error; simplemente considera que la ultima defición es la correcta.

# En la clase anterior vimos que cuando llamamos a una función, esta llamada debe de coincidir
# con los parámetros establecidos en su definición. En esta clase veremos como podemos resolver
# esto simplemente indicando el nombre de los parámetros y su valor al llamar la función, y sin
# que sea necesario respetar el orden de definición

# Cuando definimos parámetros en una función, es posible indicarle parámetros por Defecto o Default
# Esto sirve para que sea posible llamar a la función sin indicar ese parámetro; y entonces esta
# será ejecutada con los parámetros por defecto indicados

# Se pueden indicar todos los parámetros por defecto que se quieran, pero una vez que se coloca uno
# por defecto, todos los demás deben serlo

# Desplegamos Mensaje de la Clase
print ("Clase 47 Funciones Parámetros por Defecto")
print ()

# Definimos una función desplegar un mensaje
def fnMensaje(sMensaje):
   "Imprime un mensaje en la pantalla"
   print (sMensaje)
   return

# Definimos una función desplegar un mensaje
def fnMensaje(sMensaje):
   "Imprime un mensaje en la pantalla"
   print ("->:",sMensaje)
   return
   
		
# Se llama a la función
fnMensaje ("Mensaje")


# Definimos una función desplegar un mensaje
def fnMultiplica(numero1, numero2=10):
   "Multiplica 2 numeros"
   print (numero1 * numero2)
   
# Llamamos a la función
fnMultiplica(5,4)
fnMultiplica(5)
print()
   
# Definimos una función desplegar un mensaje
def fnMultiplica2(numero1=5, numero2=8):
   "Multiplica 2 numeros"
   print (numero1 * numero2)
   
# Llamamos a la función
fnMultiplica2()
fnMultiplica2(3)
fnMultiplica2(7,4)

# Definimos una función para desplegar un mensaje n veces
def fnMensajeN(sMensaje, Veces):
    for indice in range(Veces):
        print(sMensaje)

# Llamamos a la funcion con
fnMensajeN(Veces=7,sMensaje="Que tal")		
