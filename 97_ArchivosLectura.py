# Clase 97
# Archivos 3a
# Archivos Lectura

# Abrimos el archivo para lectura y escritura
# Si el archivo existe, lo abre; si no existe marca error
oArchivo = open("Datos.txt", "r")

#imprimimos una linea
while True:
   # Leemos una linea del archivo
   linea = oArchivo.readline()
   if (len(linea)==0):
       break
   print(linea,end="")    
print()
print()
print("Se ha leído todo el Archivo")

# Agregamos una linea
oArchivo.write("End\n")
input()
print()

# Cerramos el Archivo
oArchivo.close()

#Lo Abrimos de Nuevo
oArchivo = open("97_ArchivosLectura.py", "r+")
      
# Ciclo para leer todo el archivo
for linea in oArchivo.readlines():
    print (linea,end="")
print()
print()
print("Se ha leido todo el archivo")
# Close opend file
oArchivo.close()