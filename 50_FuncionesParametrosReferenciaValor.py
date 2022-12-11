# Clase 50 Parametros por Referencia o por Valor

# El Pasar parámetros por Valor o por Referencia siempre es un tema aparte en cada lenguaje
# de programación.

# Pasar un parámetro por Valor significa que la función recibe una copia de la variable original
# y aunque la copia sea modificada dentro de la función, la variable original queda intacta

# Pasar un parámetro por Referencia significa que la variable original es pasada a la función y
# los cambios son efectuados en ella directamente

# En Python, esto no existe de tal forma. Python controla esto de acuerdo a si un objeto es mutable
# o no. Ya hemos hablado de que las listas son objetos mutables, pero las tuplas no.

# A continuación veremos como los Enteros y las Cadenas son inmutables, y comprobaremos que las
# listas si lo son.

# Desplegamos Mensaje de la Clase
print ("Clase 50 Parámetros por Referencia-Valor")
print ()

# Función Consulta Empleado
def fnConsultaNumEmpleado(numEmpleado):
    
	# Imprimimos Numero de Empleado
    print("Empleado:",numEmpleado)
	
	# Lo modificamos
    numEmpleado = 20
	
	# Imprimimos Numero de Empleado
    print("Empleado:",numEmpleado)
	
	# Salimos de la Función
    return

# Declaramos la Variable
Empleado = 27

# Llamamos a la función
fnConsultaNumEmpleado(Empleado)	

# Imprimimos Numero de Empleado
print("Empleado:",Empleado)
print()


# Función Consulta Empleado
def fnConsultaNomEmpleado(nomEmpleado):
    
	# Imprimimos Numero de Empleado
    print("Empleado:",nomEmpleado)
	
	# Lo modificamos
    nomEmpleado = "Juan Perez"
	
	# Imprimimos Numero de Empleado
    print("Empleado:",nomEmpleado)
	
	# Salimos de la Función
    return

# Declaramos la Variable
Empleado = "Benito Canales"

# Llamamos a la función
fnConsultaNomEmpleado(Empleado)	

# Imprimimos Numero de Empleado
print("Empleado:",Empleado)
print()


# Función Consulta Empleado
def fnConsultaListaEmpleados(lista):
    
	# Imprimimos Numero de Empleado
    print("Lista:",lista)
	
	# Lo modificamos
    #del lista[0]
    #lista[1]="Marco Antonio"
    lista.clear()
	
	# Imprimimos Numero de Empleado
    print("Lista:",lista)
	
	# Salimos de la Función
    return	
	
# Declaramos la Variable
Empleados = ['Pedro', 'Juan', 'Alberto', 'Genaro']

# Llamamos a la función
fnConsultaListaEmpleados(Empleados)	

# Imprimimos Numero de Empleado
print("Empleados:",Empleados)
print()
