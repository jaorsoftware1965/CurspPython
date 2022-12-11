# Clase 101
# Archivos 8a
# Archivos Posicionamiento 3a parte
# Archivos Binarios Posicionamiento


# Abrimos el archivo a leer
oArchivo = open("A1_ArchivosPosicionandose3a.py","rb")

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
      
      # Obtiene el desplazamiento
      posicion = input("Posición 0-Inicio 1-Actual 2-Final:")
      
      # Verifica salida
      if (posicion==""):
         break
      
      # Solicita el desplazamiento
      desplazamiento = input("Desplazamiento:")
            
      # Se desplaza
      oArchivo.seek(int(desplazamiento),int(posicion))
          
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
      input()
      print()
      print(list(lectura))
      print()
      input()
      for codigo in lectura:
          print(chr(codigo),end="")
      input()
      print()      
      print()

# Cierra el Archivo
oArchivo.close()
# ABCDE