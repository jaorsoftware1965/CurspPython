# Clase 80 POO

# Herencia

# La herencia es la capacidad de una Clase de al ser Creada, heredar de alguna
# otra Clase que hayamos creado previamente.

# Al heredar de esa clase, tenemos acceso a las características de la Clase.

# A la clase de la cual se hereda, se le conoce como clase Padre; a la clase
# nueva que hereda, se le conoce como clase hija.

    
# Definimos Clase Accesorio
class Accesorio():
    def __init__(self):
        # Creo 3 propiedades No publicas de instancia de la Clase
        self.__deporte = "Sin Deporte"
        self.__marca   = "Sin Marca"
        self.__color   = "Sin Color"            

    def ImprimeAccesorio(self):        
        print("Deporte :",self.__deporte)
        print("Marca   :",self.__marca)
        print("Color   :",self.__color)
        #print("Algo")
        

# Definimos un Objeto
oAccesorio = Accesorio()
print("Se imprime el objeto Accesorio")
oAccesorio.ImprimeAccesorio()
input()
print()        

class PrendaVestir(Accesorio):
    def __init__(self):
        #Indispensable para que funcione la Herencia correctamente
        Accesorio.__init__(self)
        self.__talla="Sin talla"
        self.__genero="Sin Genero"
    
    def ImprimePrenda(self):
        # Imprimos la Función de la Clase Padre
        super().ImprimeAccesorio()
        print("Talla   :",self.__talla)
        print("Genero  :",self.__genero)

# Creo el Objeto de Prenda
oPrendaVestir = PrendaVestir()

# Ejecutamos un Método de su Clase Padre
print("Se imprime el objeto Accesorio desde Prenda")
oPrendaVestir.ImprimeAccesorio()
input()
print()

# Ejecutamos un Método de su Clase que llama a uno de su Padre
print("Se imprime el objeto Prenda")
oPrendaVestir.ImprimePrenda()    
input()
print()
        
# Declaramos una Clase Playera        
class Playera(PrendaVestir):
    def __init__(self):
        #Indispensable para que funciones la Herencia correctamente
        PrendaVestir.__init__(self)
        self.__manga="Sin Manga"
        self.__cuello="Sin Cuello"
        
    def ImprimePlayera(self):
        # Imprimos la Función de la Clase Padre
        super().ImprimePrenda()
        print("Manga   :",self.__manga)
        print("Cuello  :",self.__cuello)
    
# Creo el Objeto de Playera
oPlayera = Playera()

# Ejecutamos un Método de su Clase Padre
print("Se imprime el objeto Accesorio desde Playera")
oPlayera.ImprimeAccesorio()
input()
print()

# Ejecutamos un Método de su Clase que llama a uno de su Padre
print("Se imprime el objeto Prenda desde Playera")
oPlayera.ImprimePrenda()    
input()
print()

# Ejecutamos un Método de su Clase que llama a uno de su Padre
print("Se imprime el objeto Playera")
oPlayera.ImprimePlayera()    
input()
print()

