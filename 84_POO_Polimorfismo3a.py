# Clase 84 POO

# Polimorfismo 3a

# Herencia Múltiple

# Python tiene la capacidad de la Herencia Múltiple tal y como lo hace C++.
# La herencia múltiple se da cuando una clase derivada o hija, tiene
# mas de una clase base o padre

#defino PI
PI = 3.1416
    
# Definimos Clase Círculo
class Circulo():
    def __init__(self, radio):
        self.__radio = radio
        
    def area(self):
        return PI * self.__radio * self.__radio    

class Mesa():
    def __init__(self, alto):
        self.__alto = alto
        
    def altura(self):
        return self.__alto
        

class MesaRedonda(Circulo,Mesa):
    def __init__(self, radio, alto, color):        
        Circulo.__init__(self,radio)
        Mesa.__init__(self,alto)
        self.__color=color

    def color(self):
        return self.__color

# Creamos el OBjeto de la Mesa Redonda
oMesaRedonda = MesaRedonda(15,3,"Cafe")

# Despliega información de la Mesa Redonda
print("Las propiedades de la mesa son:");
print("Altura = ", oMesaRedonda.altura());
print("Area   = ", oMesaRedonda.area());
print("Color  = ", oMesaRedonda.color()); 
