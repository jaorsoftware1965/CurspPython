# Clase 81 POO

# Herencia 2a Parte
# Usando Getter's y Setter's

    
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
        

    def ImprimeAccesorio(self):        
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
oAccesorio.ImprimeAccesorio()
input()
print()

print("Se imprime desde los Getter's")
print(oAccesorio.getDeporte())
print(oAccesorio.getMarca())
print(oAccesorio.getColor())
input()
print()

        

class PrendaVestir(Accesorio):
    def __init__(self):
        #Indispensable para que funcione la Herencia correctamente
        Accesorio.__init__(self)
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
            
    def ImprimePrenda(self):
        # Imprimos la Función de la Clase Padre
        super().ImprimeAccesorio()
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

print("Se imprime desde los Getter's")
print(oPrendaVestir.getDeporte())
print(oPrendaVestir.getMarca())
print(oPrendaVestir.getColor())
print(oPrendaVestir.getTalla())
print(oPrendaVestir.getGenero())
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
        
    def ImprimePlayera(self):
        # Imprimos la Función de la Clase Padre
        super().ImprimePrenda()
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

print("Se imprime desde los Getter's")
print(oPlayera.getDeporte())
print(oPlayera.getMarca())
print(oPlayera.getColor())
print(oPlayera.getTalla())
print(oPlayera.getGenero())
print(oPlayera.getManga())
print(oPlayera.getCuello())
input()
print()
