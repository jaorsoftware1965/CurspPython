# Clase 87

# Como usar una DLL desde python

# Importamos ctypes
import ctypes as c

# acceso a la biblioteca
dll = c.CDLL("funciones.dll")

# acceso a la variable global de la biblioteca
# longitud del array
size = c.c_int.in_dll(dll, 'tam').value
print(size)

# se establece el tipo de dato (en C) que retornará la función
dll.promedio.restype = c.c_float

# de esta forma se declara un array de enteros con ctypes 
vector = c.c_int * size

# se define al array
v = vector(10,20,13,14,5,16)

# resultado
print(dll.promedio(v))