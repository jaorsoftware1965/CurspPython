# Clase 70 POO
# Creando Clases y Objetos en Python

# Para crear un objeto en Python, primeramente debemos de crear una clase

# Una clase es como una "plantilla", "receta" o "manual de construcción"
# en la cual se establecen las propiedades y métodos que tendran los
# objetos a partir de esa clase


# Para crear una clase lo hacemos con la sentencia class como sigue:
# class nombreclase():
       # propiedades y métodos de la clase
	   
# Cuando creamos una clase, hereda de la Clase Base Principal Object


# Definimos una Clase utilizando la palabra reservada class
class MiClase():
    pass
    valorX=10;

    def fnTest():
	    print("Algo")
	

# Creamos un objeto de la Clase
miObjeto = MiClase()

# Imprimimos los tipos
print("Type del Objeto  -->",type(miObjeto))
print()
print("Type de la Clase -->",type(MiClase))
input()
print()

# Las propiedades y métodos
print("Dir del objeto  -->",dir(miObjeto))
print()
print("Dir la Clase    -->",dir(MiClase))
input()
print()

print("Propiedad __module__ del objeto:",miObjeto.__module__)
print("Propiedad __init__   del objeto:",miObjeto.__init__)
input()
print()

# Accediendo a la propiedad el Método
print("El valor de X",miObjeto.valorX)
miObjeto.fnTest


