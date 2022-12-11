# Clase 77 POO

# Objetos dentro de Objetos
# Como referenciarlos


# Definimos Clase Playera
class Playera:
    def __init__(self, tipo, marca="adidas", color="Blanco"):
        # Creo las variables de instancia de la Clase
        self.tipo  = tipo
        self.marca = marca
        self.color = color

# Definimos Clase Short
class Short:
    def __init__(self, tipo, marca="adx", color="azul"):
        # Creo las variables de instancia de la Clase
        self.tipo  = tipo
        self.marca = marca
        self.color = color
        
# Definimos Clase Tenis
class Tenis:
    def __init__(self, tipo, marca="nike", color="negro"):
        self.tipo  = tipo
        self.marca = marca
        self.color = color
    
# Definimos Clase Accesorios Deportivos
class Uniforme:    
    # definimos el método para inicializar
    def __init__(self,tipo):
        self.playera = Playera(tipo)
        self.short   = Short(tipo)
        self.tenis   = Tenis(tipo)
        
    def Imprime(self):
        print("Playera")
        print("Tipo   :",self.playera.tipo)
        print("Marca  :",self.playera.marca)
        print("Color  :",self.playera.color)
        input()
        print()
        
        
        print("Short")
        print("Tipo   :",self.short.tipo)
        print("Marca  :",self.short.marca)
        print("Color  :",self.short.color)
        input()
        print()
        
        print("Tenis")
        print("Tipo   :",self.tenis.tipo)
        print("Marca  :",self.tenis.marca)
        print("Color  :",self.tenis.color)
        input()
        print()
                
# Podemos crear objetos individuales        
oPlayera = Playera("Futbol")
oShort   = Short("Futbol")
oTenis   = Tenis("Basquetbol")
        
# Declaro un Objeto
oUniforme = Uniforme("Futbol")

print (dir(oUniforme))
input()
print

print (dir(oUniforme.playera))
input()
print()


# Ejecuta el Despliegue de la Información del Uniforme
oUniforme.Imprime()

# Tambien podemos acceder directamente
print (oUniforme.tenis.tipo)
print (oUniforme.tenis.color)
print (oUniforme.tenis.marca)
