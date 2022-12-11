# Clase 100
# Archivos 7a
# Archivos Posicionamiento 2a parte

# Uso de la Función seek y tell

# Abrimos el archivo a leer
oArchivo = open("A0_ArchivosPosicionandose2a.py","r")

# Parametros de la Función seek
POS_INICIAL = 0
POS_ACTUAL  = 1
POS_FINAL   = 2

# Se mueve al final del archivo
oArchivo.seek(0,POS_FINAL)

# Obtiene la Longitud del archivo
longitud = oArchivo.tell()

# la Imprime
print("La longitud del Archivo es:",longitud)

# Se coloca de nuevo en el inicio
oArchivo.seek(0,POS_INICIAL)

#ciclo
while True:
      # Obtiene la posicion actual
      posActual = oArchivo.tell()
      print("La posición actual es:",posActual)
      print()
      
      # Solicita el desplazamiento
      desplazamiento = input("Desplazamiento (Enter para salir)")
      
      # Verifica si es salida
      if (desplazamiento ==""):
          break
      
      # Verifica si hay desplazamiento
      if (int(desplazamiento)!=0):
          # Se desplaza
          desplazamiento = posActual + int(desplazamiento)                    
          oArchivo.seek(desplazamiento,POS_INICIAL)
          
          # Obtiene la posicion actual
          posActual = oArchivo.tell()
          print("La posición actual despues de desplazamiento:",posActual)
          print()
          
      
      # Solicita caracteres a leer
      caracteres = int(input("Cuantos caracteres a leer:"))
      
      # Lee los caracteres
      lectura = oArchivo.read(caracteres)      
      print("Los caracteres leidos:")
      print(lectura)
      print()

# Cierra el Archivo
oArchivo.close      