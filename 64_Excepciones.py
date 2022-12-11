# Clase 64 Excepciones

# Los errores que se producen en una aplicación cuando esta se ejecuta
# son llamadas Excepciones.

# Para controlar esta circunstancia, python permite el manejo de estas
# excepciones de la siguiente forma:

# try:
    # En esta sección se escribe el código del cual se quiere controlar
	# el error

# except ValueError:
   # En ese caso sabemos exactamente cual es el error que puede suceder

# except (ValueError1, ValueError2):
   # Es posible manejar mas de un error en un mismo bloque de código
   
# except:
   # Manejar excepciones no contempladas en las anteriores excepciones
   
# finally:
   # Este código se ejecutará se haya o no producido el error

   
# Desplegamos Mensaje de la Clase
print ("Clase 64 Excepciones")
print ()
   

# Solicitamos la lectura de 2 numeros 
print("División entre 2 numeros \n")
a = float(input("Captura el Dividendo:"))
b = float(input("Captura el Divisor  :"))

# Tratamos de hacer la división
try:
	print ("La división es:", a/b);	
    
except ZeroDivisionError:     
   print("División entre 0 no está definida")
   
finally:
   print("Programa Terminado");   