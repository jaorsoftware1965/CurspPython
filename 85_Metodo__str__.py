# Clase 85 POO

# Redefiniendo el Método __str__

# Definimos la Clase Persona
class Persona:
    def __init__(self,nombre,apellido):
        # Propiedades de Instancia
        self.nombre=nombre
        self.apellido=apellido
    
    # Redefinimos el Método__str__    
    def __str__(self):
        # Construimos una cadena a retornar
        cadena=self.nombre+","+self.apellido
        return cadena
        
# Creamos un objeto Persona 
oPersona = Persona ("Jose","Rodriguez")

# Imprimimos el Objeto
print("Persona:",oPersona)
input()
print()

# Imprimimos usando str
print("Persona:",str(oPersona))

