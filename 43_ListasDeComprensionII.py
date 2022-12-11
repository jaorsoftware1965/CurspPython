# Clase 43 Listas de Comprensión II

# En esta clase veremos usos mas avanzados de las listas de Comprensión

# Desplegamos Mensaje de la Clase
print("Clase 43 Listas de Comprensión II")
print()

# Diccionario de Sueldos
Sueldos={"Jose":4800,"Juan":6500,"Elena":3500,"Pedro":8900}

# Imprimimos los items
print ("Lista de Sueldos")
print (Sueldos)
print (Sueldos.items())
print ()

# Obtener los Sueldos mayores de 5 mil
SueldosMay5mil=[xNombre for xNombre, xSueldo in Sueldos.items() if xSueldo >= 5000]
print ("Empleados con Sueldo Mayor a 5 mil")
print (SueldosMay5mil)
print ()

print ("Empleados con Sueldo Mayor a 5 mil Descriptivo")
SueldosMay5mil=[(xNombre,xSueldo) for xNombre, xSueldo in Sueldos.items() if xSueldo >= 5000]
print (SueldosMay5mil)
print ()

# Lista de Empleados
Empleados = [["Juan",4500,"Ventas"],["Elena",5000,"Ventas"],["Jose",4500,"Contabilidad"]]
print("Lista de Empleados")
print (Empleados)
print()

xEmpleadosVentasMay4mil = [(nombre,sueldo) for nombre,sueldo,area in Empleados if sueldo >4000 and area=="Ventas"]
print ("Empleados de Ventas que ganan mas de 4000")
print (xEmpleadosVentasMay4mil)
print ()

# Matriz de Datos
# 11 12 13
# 21 22 23
# 31 32 33
matriz = [[11,12,13],[21,22,23],[31,32,33]]

# Creo una lista vacia
xList=[]

# Defino una función
def xFun(n):       
     xList.append(n)

# Imprimiendo la Matriz
print ("Imprimiendo cada elemento de la matriz")
[[print(xDato) for xDato in fila] for fila in matriz]
print ()

print("Generando una lista con todos los elementos")
[[xFun(xDato) for xDato in fila] for fila in matriz]
print(xList)
