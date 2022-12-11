# Clase 55 Funciones Recursivas

# Python permite la recursividad en las Funciones.
# Una función es recursiva cuando se puede llamar a si misma dentro
# de su código.

# Es importante mencionar que deberá de existir una parte del código
# en la función, en la cual ya no se llame a si misma y entonces la 
# finalice.

# Analicemos el Factorial de un Número; ejemplo clasico de programacíón
# con recursividad

# !3 = 3 * 2 * 1;
# !2 = 2 * 1

# Redefiniendo 
# !3 = 3 * !2

# Definimos la función factorial
def factorial(numero):
    
    # Mensaje para indicar que numero se está evaluando
    print("Calculando el Factorial de",numero);
	
	# Verifica si es 0 o 1
    if (numero==0 or numero==1):
        resultado = 1;
        print ("Retornando (1):",resultado);
        return resultado
	
	# Para cualquier otro numero usa recursividad	
    else:
	    # Colocando el resultado en una variable
        resultado =  numero * factorial(numero-1)
		
		# Imprimimos antes de retornar
        print ("Retornando (2):",resultado);
		
		# Retornamos
        return resultado;	

# Llamando a la función factorial		
print ("El Factorial de 3:",	factorial(3))

