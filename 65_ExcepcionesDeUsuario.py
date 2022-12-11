# Clase 65 Excepciones de Usuario

# En esta clase veremos como es posible en python lanzar nuestras propias
# excepciones.

# Para lograr esto lo hacemos utilizando la palabra reservada raise en 
# conjunto con ValueError


# Definimos una función para leer el género
def leerGenero():
    
	#Leemos el Genero
    genero = input("Captura tu Género (H-M):")
    
	# Verificamos si capturo correctamente
    if (genero!= "H" and genero != "M"):

    	# Lanzamos el valor de Error
        raise ValueError("Género Incorrecto")
    
	# Retornamos el genero
    return genero

	
# Desplegamos Mensaje de la Clase
print ("Clase 65 Excepciones de Usuario")
print ()


# Solicitamos la Captura del Género	
try:
    # Llamamos a la función
    genero = leerGenero()
	
    # Imprimimos de acuerdo a lo Capturado
    if (genero=="H") :
        print("Eres un Hombre")
    else :
        print("Eres una Mujer")

# Capturamos la excepción	   
except ValueError as e:
    # Desplegamos la Excepción
    print(e)
    	
   