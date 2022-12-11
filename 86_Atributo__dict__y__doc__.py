# Clase 86

# Atributos __dict__ y __doc__

# Definimos la Clase Persona
class Persona:    
    "Clase persona"
    
    varClase="Algo"
    
    def __init__(self,nombre,apellido):
        "Constructor de la Clase"
        # Propiedades de Instancia
        self.nombre=nombre
        self.apellido=apellido
    
    # Redefinimos el Método__str__    
    def __str__(self):
        "Redefiniendo __str___"
        # Construimos una cadena a retornar
        cadena=self.nombre+","+self.apellido
        return cadena
        
        
# Creamos un objeto Persona 
oPersona = Persona ("Jose","Rodriguez")

# Imprimir el dir
print(dir(oPersona))
input()
print()


# Imprimimos dict
print("Dict de oPersona:",oPersona.__dict__)
input()
print()

# Imprimimos dict
print("Dict de Persona:",Persona.__dict__)
input()
print()


print("Doc  de oPersona:",oPersona.__doc__)
input()
print()

print("Doc de __init__:",oPersona.__init__.__doc__)
input()
print()

print("Doc de __str__:",oPersona.__str__.__doc__)
input()
print()


