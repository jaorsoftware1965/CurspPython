# Clase 24 Sentencias break continue y pass

# Existen 3 sentencias que se utilizan para controlar el comportamiento de un Ciclo while o for y son las
# sentencias break, continue y pass.

# La sentencia break simplemente rompe el ciclo de ejecución, para que el flujo del programa salga
# inmediatamente del ciclo y continúe con las instrucciones posteriores.

# La sentencia continue, hace que el flujo regrese al inicio del ciclo para evaluar de nuevo la
# condición y se ignoren las siguientes instrucciones que haya posteriores

# Hay una tercera instrucción; que es pass; que simplemente no ejecuta absolutamente nada; y según el manual
# se debe de usar en lugares donde temporalmente no se conoce el código que irá; pero se necesita escribir
# alguna instrucción para poder distribuir correctamente el código. 

# A continuación ejemplos al respecto

print("Clase 24 Sentencia break continue y pass")
print()

# Variable de Ejemplo
sLinea ="Linea 1\n. Linea 2"

# Mensaje de impresión
print("Imprimiendo Caracteres hasta fin de Línea")
print("-----------------------------------------")

# Ciclo para imprimir cada caracter de la linea hasta que se encuentre un \n
for caracter in sLinea:  

    # Verifica si es el cambio de línea
    if caracter == '\n':
       # Sale del Ciclo for
       break

    # Imprime el caracter
    print('Caracter:', caracter)
else:
    print("Fin de impresión")

# Deja una Linea
print()

# Variable para tabla de Multiplicar y multiplicador
tabla = 5
multiplicador = 0

# Mensaje
print("Tabla de Multiplicar solo con impares")
print("-----------------------------------")

# Ciclo para Imprimir
while (multiplicador < 10):              
            
      # Incrementa el Multiplicador
      multiplicador += 1

      # Verifica si el multiplicador es par
      if (multiplicador % 2 == 0):
         
         # Ignora las instrucciones siguiente y regresa al principio del Ciclo
         continue
      
      # Imprime la tabla
      print(tabla,"X",multiplicador,"=",tabla*multiplicador)            

else:
    # No ejecuta nada, solo para indicar fin del ciclo while
    pass

# Mensaje con el Fin del Programa
print("Fin del Programa")