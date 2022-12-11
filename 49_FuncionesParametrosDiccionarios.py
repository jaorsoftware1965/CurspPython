# Clase 49 Funciones Parámetros Diccionarios

# En esta clase veremos como utilizar Diccionarios como Parámetros en forma tradicional
# y en forma especial

# Desplegamos Mensaje de la Clase
print ("Clase 49 Funciones Parámetros Diccionarios")
print ()


# Define la función
def fnEmpleadosDespliega(**Empleados):
    # Imprime los datos y el tipo
    print (Empleados)
    print (type(Empleados))
	
	#Imprime los datos del Diccionarios
    for xKey, xVal in Empleados.items():
        print("Nombre:",xKey, "Edad:",xVal)
    print()

# Se ejecuta la función
fnEmpleadosDespliega(Juan=22,Alberto=30,Jose=45)


# Función para porcentaje de
def fnProductosConIva(iva, **productos):
	for xProducto, xPrecio in productos.items():
		print (xProducto, xPrecio * (1+iva))
	print ()
		
# Despliega los productos con iva
fnProductosConIva(.15, Lapiz = 2.50, Goma = 4.5, Pegamento = 21)


# Define la función
def fnEmpleadosDespliega2(Empleados):
    # Imprime los datos y el tipo
    print (Empleados)
    print (type(Empleados))
    
	#Imprime los datos del Diccionarios
    for xKey, xVal in Empleados.items():
        print("Nombre:",xKey, "Edad:",xVal)
    print()


# Definimos un Diccionario de Edades
dicEdades ={"juan":34, "Elsa":25, "Ramiro":45,"Juan":29}

fnEmpleadosDespliega2(dicEdades)


