# Clase 95
# Archivos Apertura y Cierre

# Declaramos abrimos un archivo de escritura
try:

    # Abrimos el Archivo
    archivo = open("94_Archivos.py","r")
    
    print("El Archivo ha sido abierto")
    input()
    print()

    #Imprimimos archivo
    print("El Objeto Archivo:",archivo)
    input()
    print()

    #Imprimimos atributos del archivo
    print("Nombre:",archivo.name)
    print("Cerrado:",archivo.closed)
    print("Modo:",archivo.mode)
    input()
    print()

    #Cerramos el Archivos
    archivo.close()
    print("El archivo se ha cerrado")
    input()
    print()

    #Imprimimos atributos del archivo
    print("Nombre:",archivo.name)
    print("Cerrado:",archivo.closed)
    print("Modo:",archivo.mode)
    input()
    print()

except FileNotFoundError:     
   print("El Archivo no se encontró")



