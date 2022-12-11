# Clase 66 Excepciones Trace

# En esta clase veremos como es posible en python realizar un trace; es decir
# un seguimiento de donde se produce una excepcion

# Para lograr esto importamos la librería traceback

# Importamos la Librería
import traceback
	
# Definimos una función
def myfun():
 
    # Definimos una función dentro de otra 
    def myfun2():

		# Capturamos la excepción
        try:
		    # Ejecutamnos una divisón entre 0
            3 / 0
            
		# Capturamos la Excepción	
        except ZeroDivisionError as e:
            print("La excepcion:");
            print(e)
            print()
            print("La Clase:")
            print("Class:", e.__class__)
            print()
            
            print("Seguimiento de la Excepción")
			# Imprimiendo el seguimiento de la excepción
            for line in traceback.format_stack():
                print(">",line.strip())
                
        
	# Ejecutamos la función	
    myfun2()  
    
        
# Definimos una función de Test		
def test():
    myfun()
        

# Desplegamos Mensaje de la Clase
print ("Clase 66 Trace")
print ()

# Ejecutamos la función
test()    
