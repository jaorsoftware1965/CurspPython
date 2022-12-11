# Clase 56 Funciones Recursivas 2a parte
# Función recursiva para adivinar un numero


# Definimos 
def adivina(intentos, numero):
    
    # Mensaje para solicitar un numero
    respuesta = input('Adivina el Numero que estoy pensando: ')
		
    # Verifica si es 0 o 1
    if (respuesta == numero):        
        print ("! Has Adivinado !");        		
    else:
        # Verifica intentos
        if (intentos > 1):
            print ("Has fallado, intentalo otra vez")
            adivina(intentos-1,numero)
        else:
            print ("Has fallado y no tienes mas intentos");

    print("Saliendo", intentos)
	
# Llamando a la función factorial		
adivina(3,"7")

