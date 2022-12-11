# Clase 67 Entrada de Datos

# En esta clase veremos ya formalmente la entrada de datos en Python
# ya que en algunas clases recientes hemos hecho ya uso de la función
# input que es la que se utiliza con este propósito.

# Como hemos observado la función input() realiza entrada de datos por
# el teclado y esto al asignarlo a una variable, los datos son recibidos
# como una cadena.

# Si queremos darle un uso distinto a lo capturado tenemos que hacer 
# una conversión de datos.

print("Clase 67 Entrada de Datos")
print("-----------------------------")
print()

#Leyendo el Nombre
print("Captura tu nombre:")
nombre = input()

#Leyendo apellido
apellido = input(f"{nombre}, ahora captura tu apellido:")

#Leyendo la Edad
edad = int(input(f"{nombre} {apellido}, captura tu edad:"))

#Leyendo el Peso
peso = float(input(f"{nombre} {apellido}, captura tu peso:"))

#Leyendo estatura
estatura = float(input(f"{nombre} {apellido}, captura tu estatura:"))

print("Tus Datos son:")
print("Nombre   :",nombre)
print("Apellido :",apellido)
print("Edad     :",edad)
print("Peso     :",peso)
print("Estatura :",estatura)
print()

print("Los Tipos de Datos son:")
print(type(nombre))
print(type(apellido))
print(type(edad))
print(type(peso))
print(type(estatura))
