# Clase 91
# Generadores

# Un generador es una función que definimos y que nos permite, retornar
# n veces uno o mas valores y detener la ejecución de la función cada vez
# que se ejecuta el retorno de cada valor

# Para poder lograr una función que sea un generador, hacemos uso de
# la palabra reservada yield, la cual es la que controla la información
# que va a retornar el generador

# Cuando se ejecuta yield, el valor es devuelto y la función se detiene
# y continuará su ejecución mientras haya otro valor yield que retornar
# cuando se vuelva a llamar

# Funcion que genera únicamente 2 numeros
def genera2():
   
   # Devuelve el primero
   yield 5
   
   # Devuelve el segundo numeros
   yield 20
   
# Llamamos a la función para obtener el generador
numero = genera2()

# Verificamos que nos devuelve numero
print("Lo que devuelve numero:")
print (numero)
input()
print()

print("Lo que devuelve dir:")
print (dir(numero))
input()
print()

print("El nombre de la Clase:")
print (numero.__class__)
input()
print()

# Obtenemos el Primer Numero Generado
print("El Primer numero:")
print(next(numero))
input()
print()

print("El Segundo numero:")
print(next(numero))
input()
print()


# Esta tercer llamada fallará
print("La tercera llamada falla:")
try:
    print(next(numero))
except StopIteration:
    print("Ya no hay mas datos en el Generador")