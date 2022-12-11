# Clase 82 POO

# Polimorfismo
# El polimorfismo es la capacidad de redefinir un método en una clase
# hija o derivada; para que en esta tenga un comportamiento distinto.

    
# Definimos Clase Accesorio
class Accesorio():
    def __init__(self):
        # Creo 3 propiedades No publicas de instancia de la Clase
        self.__deporte = "Sin Deporte"
        self.__marca   = "Sin Marca"
        self.__color   = "Sin Color"            
        
    def setDeporte(self,deporte):
        self.__deporte = deporte
    
    def setMarca(self,marca):
        self.__marca = marca
        
    def setColor(self,color):
        self.__color = color
    
    def getDeporte(self):
        return self.__deporte
    
    def getMarca(self):
        return self.__marca
        
    def getColor(self):
        return self.__color
        

    def Imprime(self):        
        print("Deporte :",self.__deporte)
        print("Marca   :",self.__marca)
        print("Color   :",self.__color)
       
        

# Definimos un Objeto
oAccesorio = Accesorio()

# Establecemos valores
oAccesorio.setDeporte("Futbol")
oAccesorio.setMarca("Adidas")
oAccesorio.setColor("Azul")

print("Se imprime el objeto Accesorio")
oAccesorio.Imprime()
input()
print()
        

class PrendaVestir(Accesorio):
    def __init__(self):
        #Indispensable para que funcione la Herencia correctamente
        Accesorio.__init__(self)  ## Debido a que hemos redefinido el constructor
        self.__talla="Sin talla"
        self.__genero="Sin Genero"
        
    def setTalla(self,talla):
        self.__talla = talla
        
    def setGenero(self,genero):
        self.__genero = genero
    
    def getTalla(self):
        return self.__talla
    
    def getGenero(self):
        return self.__genero
            
    def Imprime(self):
        # Imprimos la Función de la Clase Padre
        super().Imprime()
        print("Talla   :",self.__talla)
        print("Genero  :",self.__genero)

# Creo el Objeto de Prenda
oPrendaVestir = PrendaVestir()

# Establecemos valores
oPrendaVestir.setDeporte("BasquetBol")
oPrendaVestir.setMarca("Nike")
oPrendaVestir.setColor("Rojo")
oPrendaVestir.setTalla("M")
oPrendaVestir.setGenero("Unisex")

# Ejecutamos un Método de su Clase que llama a uno de su Padre
print("Se imprime el objeto Prenda")
oPrendaVestir.Imprime()    
input()
print()

        
# Declaramos una Clase Playera        
class Playera(PrendaVestir):
    def __init__(self):
        #Indispensable para que funciones la Herencia correctamente
        PrendaVestir.__init__(self)
        self.__manga="Sin Manga"
        self.__cuello="Sin Cuello"

    def setManga(self,manga):
        self.__manga = manga
        
    def setCuello(self,cuello):
        self.__cuello = cuello
    
    def getManga(self):
        return self.__manga
    
    def getCuello(self):
        return self.__cuello
        
    def Imprime(self):
        # Imprimos la Función de la Clase Padre
        super().Imprime()
        print("Manga   :",self.__manga)
        print("Cuello  :",self.__cuello)
    
# Creo el Objeto de Playera
oPlayera = Playera()

# Establecemos valores
oPlayera.setDeporte("Beisbol")
oPlayera.setMarca("ADX")
oPlayera.setColor("Blanco")
oPlayera.setTalla("G")
oPlayera.setGenero("Hombre")
oPlayera.setManga("Larga")
oPlayera.setCuello("V")


# Ejecutamos un Método de su Clase que llama a uno de su Padre
print("Se imprime el objeto Playera")
oPlayera.Imprime()    
input()
print()

