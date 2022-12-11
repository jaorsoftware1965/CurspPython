# Clase 15 Operador de Formato a Cadenas

# Una de las características mas interesantes para el manejo de cadenas, es el formateo utilizando
# el Operador %. Este operador es de uso único para las cadenas y tiene una gran cantidad de funciones
# similares al uso de la función printf del lenguaje C.

# Veamos el siguiente ejemplo que muestra su uso
# print("El Nombre del Empleado es: %s y su Edad es: %d años " %('Juan', 29))

# En el ejemplo anterior, dentro de la Cadena del Mensaje se utiliza el operador % en 2 lugares específicos
# para indicar que ahí se deberán de colocar valores correspondiente. Estos valores se encuentran indicados
# posterior a la cadena; seguido de otro operador % y entre paréntesis y separados por ","; los valores que
# se colocarán dentro de la cadena en lugar del operador.

# El primer  operador %s indica que se deberá de colocar una cadena en lugar del operador
# El segundo operador %d indica que se deberá de colocar un valor numérico en lugar del operador

# A continuación la tabla con cada uno de los posibles operadores

# Operador      Conversión
#   %c          Caracter
#   %s          Cadena
#   %i          Entero Decimal con Signo
#   %d          Entero Decimal con Signo
#   %u          Entero Decimal sin Signo
#   %o          Entero Octal
#   %x          Entero Hexadecimal en minúsculas
#   %X          Entero Hexadecimal en mayúsculas
#   %e          Notación Exponencia con minúscula 'e'
#   %E          Notación Exponencia con mayúscula 'E'
#   %f          Numero Real en punto flotante
#   %g          Redondea la última cifra decimal a partir de .5
#   %G          Redondea la última cifra decimal a partir de .5


# Desplegamos Mensaje de la Clase
print("Clase 15 Operador de Formato a Cadenas")

print("El Caracter es:%c" %('K'))
print("El Caracter es:%c" %(64))
print()

print("El Nombre del Empleado es: %s y su Edad es: %d años " %('Juan', 29))
print("El Precio del Producto es: %f " %(29.50))
print()

print("La Distancia es: %e " %(234429.50))
print("La Distancia es: %E " %(234429.50))
print()

print("El Número 20 en Octal es:%o" %(20))
print("El Número 30 en Hexad es:%x" %(30))
print("El Número 30 en Hexad es:%X" %(30))
print()

print("Redondea : %G " %(2344.2950))
print("Redondea : %G " %(2344.2940))
print("Redondea : %G " %(234429.50))
print("Redondea : %G " %(234429.40))