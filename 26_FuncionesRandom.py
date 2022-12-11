# Clase 26 Funciones Random

# A continuación veremos un conjunto de instrucciones que se utilizan para generar números
# aleatorios; y para aleatoriamente cambiar el orden en una secuencia.
# Para utilizar estos métodos, haremos uso del Módulo random

# Mensaje de impresión
print("Clase 26 Funciones Random")
print("-----------------------------")
print()

# Importamos el Módulo 
import random

# Obteniendo un elemento de una secuencia o colección de datos
print("choice(1, 2, 3, 5, 9) : ", random.choice([1, 2, 3, 5, 9]))
nombres=["juan","alberto","pedro","Gerardo","Martina","Diana","Carolina"]
print("choice(",nombres,") : ", random.choice(nombres))
print("choice('A String') : ", random.choice('A String'))
print()

print("Numero aleatorio entre 0 y 10 =>",random.choice(range(0,11)))
print("Numero aleatorio entre 0 y 10 =>",random.choice(range(0,11)))
print("Numero aleatorio entre 0 y 10 =>",random.choice(range(0,11)))
print("Numero aleatorio entre 0 y 10 =>",random.choice(range(0,11)))
print("Numero aleatorio entre 0 y 10 =>",random.choice(range(0,11)))
print()

print("Numero aleatorio par entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 2))
print("Numero aleatorio par entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 2))
print("Numero aleatorio par entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 2))
print("Numero aleatorio par entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 2))
print("Numero aleatorio par entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 2))
print()

print("Numero aleatorio multiplo de 3 entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 3))
print("Numero aleatorio multiplo de 3 entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 3))
print("Numero aleatorio multiplo de 3 entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 3))
print("Numero aleatorio multiplo de 3 entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 3))
print("Numero aleatorio multiplo de 3 entre 0  y 10 incluyendo el 0 =>",random.randrange(0, 10, 3))
print()

print("Numero aleatorio fraccionario mayor que 0 y menor que 1 =>",random.random())
print("Numero aleatorio fraccionario mayor que 0 y menor que 1 =>",random.random())
print("Numero aleatorio fraccionario mayor que 0 y menor que 1 =>",random.random())
print("Numero aleatorio fraccionario mayor que 0 y menor que 1 =>",random.random())
print("Numero aleatorio fraccionario mayor que 0 y menor que 1 =>",random.random())
print()

# Random en un intervalo específico
print("Numero aleatorio fraccionario mayor que 2 y menor que 5 =>",random.uniform(2,5))
print("Numero aleatorio fraccionario mayor que 2 y menor que 5 =>",random.uniform(2,5))
print("Numero aleatorio fraccionario mayor que 2 y menor que 5 =>",random.uniform(2,5))
print("Numero aleatorio fraccionario mayor que 2 y menor que 5 =>",random.uniform(2,5))
print("Numero aleatorio fraccionario mayor que 2 y menor que 5 =>",random.uniform(2,5))
print()

# Define un objeto
random.shuffle(nombres)
print("Nombres: ",nombres)
random.shuffle(nombres)
print("Nombres: ",nombres)
random.shuffle(nombres)
print("Nombres: ",nombres)
print()

# Inicializa la Semilla
random.seed(10)
print("Random numero con seed 10 : ", random.random())
print("Random numero con seed 10 : ", random.random())
print("Random numero con seed 10 : ", random.random())
print()

# Inicializa la Semilla
random.seed(10)
print("Random numero con seed 10 : ", random.random())
print("Random numero con seed 10 : ", random.random())
print("Random numero con seed 10 : ", random.random())

