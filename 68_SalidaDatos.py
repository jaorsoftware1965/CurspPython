# Clase 68 Salida de Datos

# La salida de datos en un programa de python se realiza a través
# de la sentencia print como lo hemos estado utilizando previamente
# en este curso

# En esta clase veremos ya formalmente el uso de esta instrucción
# y algunas otras formas de utilizarla adicionales a como lo hemos hecho

print("Clase 68 Salida de Datos")
print("-----------------------------")
print()

# Imprimiendo un Mensaje entre comillas
print('Hola')

# Imprimiendo mas de un elemento separado por comas
print("Hola", "Adios",50, 123.45,10)
# Para generar una línea en blanco, se puede escribir una orden print() sin argumentos.
print()
input()


# print agrega un cambio de linea siempre al final; 
# en otra instrucción veremos como evitar este cambio de linea
print("Hola", end="")
print("Adios")
print()
input()


print("Un tipo le dice a otro: \"¿Cómo estás?\"")
print('Y el otro le contesta: \'¡Pues anda que tú!\'')
print()
input()

print("Un tipo le dice a otro: '¿Cómo estás?'")
print('Y el otro le contesta: "¡Pues anda que tú!"')
print()
input()

# Incluyendo variables o expresiones como argumento, lo que nos permite combinar 
# texto y variables:

# Asigno un Nombre
nombre = "Juan"
edad = 33
print("Me llamo", nombre, "y tengo", edad, "años.")
print()
input()


# Combinando 
semanas = 5
print("En", semanas , "semanas hay", 7 * semanas, "días.")
print()
input()


print("¡Hola,", nombre, "!")
print(f"¡Hola, {nombre} han pasado {semanas} semanas sin saludarte")
print()
input()
