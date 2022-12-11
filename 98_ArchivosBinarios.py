# Clase 98
# Archivos 4a
# Archivos Binarios

# Abrimos el Archivo Origen y el Destino
oArchivoOrigen  = open("Curso_Python_Clase_00-53.rar", "rb")
oArchivoDestino = open("Curso_Python_Clase_00-53_Copy.rar","wb")

# Variable para contar los bytes
cuentaBytes=0

#Ciclo de Lectura
while True:
   # Leemos un byte del archivo
   byte = oArchivoOrigen.read(1)
   if (len(byte)==0):
       break   
   #print(byte,end="")
   #input()
   # Grabamos al archivo destino
   oArchivoDestino.write(byte)   
   cuentaBytes = cuentaBytes + 1
print()
print("Se ha copiado el archivo")
print("Bytes copiados:",cuentaBytes)


# Cerramos los 2 archivos
oArchivoOrigen.close()
oArchivoDestino.close()
