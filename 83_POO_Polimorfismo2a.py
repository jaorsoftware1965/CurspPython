# Clase 83 POO

# Polimorfismo 2a parte
# Métodos Virtuales en C++

# El Ejemplo Clásico
    
# Importamos este modulo
from math import *

    
# Definimos Clase Figura 
class Figura(object):
    " Una figura en el plano. "
    def area(self):
        " Este método debe ser redefinido. "
        pass
    def perimetro(self):
        " Este método debe ser redefinido. "
        pass
            

class Circulo(Figura):
    " Un círculo en el plano. "
    def __init__(self, radio):
        " Constructor de círculo. "
        self.radio = radio
 
    def area(self):
        " Devuelve el área del círculo. "
        return pi * self.radio * self.radio        
    
    def perimetro(self):
        " Devuelve el perimetro del círculo. "
        return pi * self.radio * 2            
        
class Rectangulo(Figura):
    " Un Rectángulo en el plano. "
    def __init__(self, base, altura):
        " Constructor de triángulo. "
        self.base = base
        self.altura = altura
 
    def area(self):
        " Devuelve el área del rectángulo. "
        return self.base * self.altura        
    
    def perimetro(self):
        " Devuelve el perimetro del rectángulo. "
        return (self.base + self.altura) * 2
        
class Triangulo(Figura):
    " Un triángulo en el plano. "
    def __init__(self, base, altura):
        " Constructor de triángulo. "
        self.base = base
        self.altura = altura
 
    def area(self):
        " Devuelve el área del triángulo. "
        return self.base * self.altura / 2.        
    
    def perimetro(self):
        " Devuelve el perímetro del triángulo. "
        return 2*sqrt(pow(self.altura,2)+pow((self.base/2),2))+self.base
        

# Creamos un objeto para el Círculo
oCirculo = Circulo(5)

# Cálculamos el área
print("Círculo")
print("Área      : ",oCirculo.area())
print("Perímetro : ",oCirculo.perimetro())
input()
print()


# Creamos un objeto para el Rectángulo
oRectangulo = Rectangulo(5,8)

# Cálculamos el área
print("Rectángulo")
print("Área      : ",oRectangulo.area())
print("Perímetro : ",oRectangulo.perimetro())
input()
print()


#Creamos un objeto para el Triángulo
oTriangulo = Triangulo(2,7)


# Cálculamos el area
print("Triángulo")
print("Área      :",oTriangulo.area())
print("Perímetro :",oTriangulo.perimetro())
input()
print()
