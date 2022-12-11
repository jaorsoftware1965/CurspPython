# Clase 16 Simbolos Formato Cadenas

# En esta clase veremos el uso de Símbolos o Caracteres Especiales, que son utilizados para dar formato
# utilizando la instrucción print. Esto símbolos son utilizados con el operador de formato % visto en la
# clase anterior.

# A continuación la tabla de estos símbolos

# ----------------------------------------------------
# Simbolo       Explicación
# ----------------------------------------------------
#   *           Indicar precisión desde los Argumentos
#   -           Justificar a la Izquierda la Cadena
#   +           Desplegar el signo del valor numérico
#   0           Para llenar con 0's los espacios
#   ()          Referencias desde objetos

# Desplegamos Mensaje de la Clase
print("Clase 16 Simbolos para Formato de Cadenas")
print()

# Longitud
print("El Nombre del Empleado es: [%10s]" %('Juan'))
print("La Edad   del Empleado es: [%10d]" %(29))
print("El Nombre del Empleado es: [%-10s]" %('Juan'))
print("La Edad   del Empleado es: [%-10d]" %(29))
print("El Nombre del Empleado es: [%-*s]" %(5,'Juan'))
print("La Edad   del Empleado es: [%-*d]" %(5, 29))
print()

# Que aparezca en Signo en los Números
print("La Edad   del Empleado es: [%+d]" %( 29))
print("La Edad   del Empleado es: [%+d]" %( -29))
print("La Edad   del Empleado es: [%05d]" %( 29))
print("La Edad   del Empleado es: [%+05d]" %( -29))
print()

# Truncando Cadenas
print("El Nombre del Empleado es: [%10s]"  %('Este es un Mensaje largo'))
print("El Nombre del Empleado es: [%.10s]" %('Este es un Mensaje largo'))
print()

# Formateando Valores Decimales
print("El Precio del Producto es: [%9.2f]" %(341.759))
print("El Precio del Producto es: [%09.2f]" %(341.759))
print("El Precio del Producto es: [%+9.2f]" %(-341.759))
print("El Precio del Producto es: [%+09.2f]" %(-341.759))
print()

# Objeto con pares ordenados de datos
datos1={'fruta':'manzana','color':'rojo'}
datos2={'edad':33,'peso':78.50}

# Imprimiendo desde los datos con placeholders
print("La fruta : %(fruta)s es de color %(color)s" %(datos1))
print("La edad  : %(edad)05d  el peso es %(peso)07.2f" %(datos2))
