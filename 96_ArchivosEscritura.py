# Clase 96
# Archivos 2a
# Archivos Escritura

# Modo de apertura w = write = escritura
# Abre un archivo para escritura.
# Sobreescribe el archivo si existe
# Si no existe lo crea

# Creamos una archivo de escritura
aEscritura = open("Datos.txt", "w")

linea = input("Captura algo para grabar al archivo:\n")
aEscritura.write(linea+"\n");
aEscritura.write("Grabamos directamente\n");

# Solicitamos otra linea
linea = input("Captura algo mas para grabar al archivo:\n")
aEscritura.write(linea+"\n");
aEscritura.write("Grabamos directamente otra vez\n");

# Close opend file
aEscritura.close()

