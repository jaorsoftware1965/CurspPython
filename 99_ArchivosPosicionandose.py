# Clase 99
# Archivos 6a
# Archivos Posicionamiento

# Uso de la Función seek y tell

# Abrimos el archivo a leer
oArchivo = open("99_ArchivosPosicionandose.py","r")

# Parametros de la Función seek
POS_INICIAL = 0
POS_ACTUAL  = 1
POS_FINAL   = 2

# Intentamos posicionarnos al inicio del archivo
oArchivo.seek(0,POS_INICIAL)
posicion = oArchivo.tell()
print("1 >",posicion)
input()

oArchivo.seek(10,POS_INICIAL)
posicion = oArchivo.tell()
print("2 >",posicion)
input()

#oArchivo.seek(-5,POS_INICIAL) #Error


oArchivo.seek(0,POS_ACTUAL)
posicion = oArchivo.tell()
print("4 >",posicion)
input()

#oArchivo.seek(-10,POS_ACTUAL) #Error

oArchivo.seek(0,POS_FINAL)
posicion = oArchivo.tell()
print("5 >",posicion)
input()

oArchivo.seek(0,POS_FINAL) #Error