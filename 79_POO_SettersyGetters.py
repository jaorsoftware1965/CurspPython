# Clase 79 POO

# Setter's y Getter's

# Definimos Clase Accesorio
class Accesorio:
    def __init__(self):
        # Creo las propiedades No públicas de instancia de la Clase
        self.__tipo    = ""
        self.__deporte = ""
        self.__marca   = ""
        self.__color   = ""
        
    # Setter's    
    def setTipo(self,tipo):        
        #self.__tipo = tipo
        if (tipo!="Camiseta" and tipo!="Short" and tipo!="Tenis"):
            print("Error en Tipo")
            input()
        else:
            self.__tipo=tipo

    def setDeporte(self,deporte):
        self.__deporte = deporte
        
    def setMarca(self,marca):
        self.__marca = marca
        
    def setColor(self,color):
        self.__color = color
        
    # Getter's    
    def getTipo(self):                
        return "Tipo:"+self.__tipo

    def getDeporte(self):
        return self.__deporte
        
    def getMarca(self):
        return self.__marca
        
    def getColor(self):
        return self.__color

    def Imprime(self):
        print("Tipo    :",self.__tipo)
        print("Deporte :",self.__deporte)
        print("Marca   :",self.__marca)
        print("Color   :",self.__color)
        input()
        print()

# Creamos un objeto
oAccesorio = Accesorio()

# Colocamos los datos
oAccesorio.setTipo("Camiseta")
#oAccesorio.__tipo="Otra"
oAccesorio.setDeporte("Basquetbol")
oAccesorio.setMarca("Adidas")
oAccesorio.setColor("Azul")

#Imprime
oAccesorio.Imprime()

# Accedemos a través de los Getters
print("Tipo    :",oAccesorio.getTipo())
#print(oAccesorio.__tipo)
print("Deporte :",oAccesorio.getDeporte())
print("Marca   :",oAccesorio.getMarca())
print("Color   :",oAccesorio.getColor())
input()

#print(dir(oAccesorio))