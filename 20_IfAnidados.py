# Clase 20 if anidados

# En la Clase anterior vimos como utilizar la sentencia if.
# En esta clase veremos como es posible tener sentencias if's anidadas. Esto quiere decir que
# se escriben sentencias if's dentro de otras sentencias if.

print("Clase 20 if's anidados")
print()

# Declaramos algunas variables para el Ejemplo
edad = 20
sexo = "M"
estatura = 1.70

# Verifica si es mayor de edad
if (edad >= 18) :
   print("Eres mayor de Edad")
   print("Ya puedes obtener tu credencial de elector")      
   if (sexo == "M"):
      print("Debes realizar tu Servicio Militar")
   if (estatura >= 1.75):
      print("Puedes Ingresar al Ejército o Marina de México")   
   else:    
        if (edad > 15):
            print("Debes estar en la Preparatoria")
        elif (edad > 11):   
            print("Debes estar en la Secundaria")
        elif (edad > 5):
            print("Debes estar en la Primaria")
        elif (edad > 3):
            print("Debes estar en la Pre-primaria")
        else:
            print("Estás en Maternal")