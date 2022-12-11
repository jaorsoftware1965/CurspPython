# Clase 69 POO
# Programación Orientada a Objetos

# Todo en Python es un Objeto

# ¿ Que es un Objeto ?

# Definiendo en forma sencilla, un objeto es un espacio en Memoria el cual 
# tiene almacenado propiedades (variables) y métodos (funciones)

# Todo en Python es un Objeto y lo veremos a continuación


# Importamos un Módulo
import sys

# Definimos una Función
def function():
    pass


# Desplegamos sus tipos	
print(type(1))
print(type(""))
print(type([]))
print(type({}))
print(type(()))
print(type(object))
print(type(function))
print(type(sys))
input()

# Propiedades y Métodos del objeto
print("Propiedades y Métodos del Módulo")
print(dir(sys))
input()

print("Ejecutando Métodos ...")
print(sys.is_finalizing())
print(sys.getwindowsversion())
print(sys.winver)
input()

print(dir([]))
input()
