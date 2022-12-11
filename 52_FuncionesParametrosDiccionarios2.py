# Clase 52 Funciones Parámetros Diccionarios 2

# En esta clase veremos como utilizar Diccionarios como Parámetros pero haciendo referencia
# a los nombres de los argumentos de la función.

# Para este caso, la función se declara normalmente sin ninguna indicación especial; pero al
# llamarla se debe de colocar "**" antes del diccionario que contiene los nombres y valores
# de los parámetros

# Desplegamos Mensaje de la Clase
print ("Clase 52 Funciones Parámetros Diccionarios 2")
print ()


# Define la función
def fnEmpleadosDespliega(nombre, area, sueldo):
    # Imprime los datos
	print ("Los datos del Empleado son:")
	print ("Nombre :",nombre)
	print ("Area   :",area)
	print ("Sueldo :",sueldo)
	print ()
	


# Definimos un Diccionaro con los parámetros
dicEmpleado ={"nombre":"Juan", "area":"Informatica","sueldo":14500}

#Llamamos a la función con ** previos al parámetro
fnEmpleadosDespliega(**dicEmpleado)


# Define la función
def fnEmpleadosDespliega2(numero, nombre, area, sueldo):
    
	# Imprime los datos
	print ("Los datos del Empleado son:")
	print ("Numero :",numero)
	print ("Nombre :",nombre)
	print ("Area   :",area)
	print ("Sueldo :",sueldo)
	print ()

# Llamamos a la función con ** previos al parámetro
fnEmpleadosDespliega2(24,**dicEmpleado)

# Define la función
def fnEmpleadosDespliega3(numero, nombre, area, peso):
    
	# Imprime los datos
	print ("Los datos del Empleado son:")
	print ("Numero :",numero)
	print ("Nombre :",nombre)
	print ("Area   :",area)
	print ("Sueldo :",sueldo)
	print ("Peso   :",peso)
	print ()

# Llamamos a la función con ** previos al parámetro
fnEmpleadosDespliega3(24,**dicEmpleado,peso=78.500)
