# Clase 78 POO

# Métodos dentro de Objetos
# Como referenciarlos


# Definimos Clase Playera
class Playera:
    def __init__(self, tipo, marca="adidas", color="Blanco"):
        # Creo las variables de instancia de la Clase
        self.tipo  = tipo
        self.marca = marca
        self.color = color
        
    # Setter's    
    def fnSetTipo(self,tipo):
        self.tipo = tipo
                
    def fnSetMarca(self,marca):
        self.marca = marca
        
    def fnSetColor(self,color):
        self.color = color
        
# Definimos Clase Short
class Short:
    def __init__(self, tipo, marca="adx", color="azul"):
        # Creo las variables de instancia de la Clase
        self.tipo  = tipo
        self.marca = marca
        self.color = color
     
    # Setter's    
    def fnSetTipo(self,tipo):
        self.tipo = tipo
                
    def fnSetMarca(self,marca):
        self.marca = marca
        
    def fnSetColor(self,color):
        self.color = color     
        
# Definimos Clase Tenis
class Tenis:
    def __init__(self, tipo, marca="nike", color="negro"):
        self.tipo  = tipo
        self.marca = marca
        self.color = color
    
    # Setter's    
    def fnSetTipo(self,tipo):
        self.tipo = tipo
                
    def fnSetMarca(self,marca):
        self.marca = marca
        
    def fnSetColor(self,color):
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
                
        
# Declaro un Objeto
oUniforme = Uniforme("Futbol")


# Ejecuta el Despliegue de la Información del Uniforme
oUniforme.Imprime()


# Mensaje 
print("Establecemos los Tipos Colores y Marca")
input()
print()

# Establezco el Tipo
oUniforme.playera.fnSetTipo("Basquetbol")
oUniforme.short.fnSetTipo("Basquetbol")
oUniforme.tenis.fnSetTipo("Basquetbol")

# Establezco el Color
oUniforme.playera.fnSetColor("Amarillo con Franjas Azules")
oUniforme.short.fnSetColor("Azules con Franajas Amarillas")
oUniforme.tenis.fnSetColor("Blancos con Rojo")

# Establezco la Marca
oUniforme.playera.fnSetMarca("Converse")
oUniforme.short.fnSetMarca("Decatlon")
oUniforme.tenis.fnSetMarca("Superfaro")

# Ejecuta el Despliegue de la Información del Uniforme
oUniforme.Imprime()
