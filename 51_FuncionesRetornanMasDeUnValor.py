# Clase 51 Funciones que Retornan mas de un Valor

# Desplegamos Mensaje de la Clase
print ("Clase 51 Funciones que Retornan mas de un Valor")
print ()

# Función Consulta Empleado
def fnConsultaEmpleado(numEmpleado):
    
    # Retorna el Nombre, Area y Salario
    return ("Juan Perez","Contabilidad",8500,88.500)

# Llamamos a la función y asignamos a 4 variables
Nombre, Area, Sueldo = fnConsultaEmpleado(5)

# Desplegamos los Datos
print("Nombre:",Nombre)
print("Area  :",Area)
print("Sueldo:",Sueldo)
#print("Peso  :",Peso)
print()
input()

# Desplegamos los Tipos de Datos
print(type(Nombre))
print(type(Area))
print(type(Sueldo))
print(type(Peso))
print()
input()


# Colocamos todo en una sola variable
Info = fnConsultaEmpleado(5)
print (Info)
print (type(Info))
