# Clase 22 Ciclo for

# Otra de las sentencias comunes e importantes en los lenguajes de programación, es el ciclo for.
# El ciclo for en Python, no se utiliza como comunmente en otros lenguajes, en donde se itera a través
# de un valor numérico el cual va incrementando o decrementando hasta que se cumpla una condición.

# En Python, el ciclo for; se utiliza para iterar a través de colecciones de datos o de rangos.
# Al momento de lo aprendido, las variables de cadena, y otro objeto al que he llamado temporalmente
# vector o arreglo, son los únicos objetos que son una una colección de datos que podemos utilizar 
# para demostrar el uso del ciclo for. Mas adelante veremos otros objetos que tambien
# son colecciones de datos.

# La sintaxis para usar el ciclo for (que tambien es una palabra reservada) es la siguiente:
# for iterating_var in sequence:
#     sentencias
# [else:]
#     sentencias cuando termina el ciclo

# Lo anterior quiere decir que la variable iterating_var; va a tomar cada uno de los valores que se encuentren
# en sequence; que es una colección o secuencia de datos, o un rango.

# Para cada valor que tome iterating_var, se ejecutaran las sentencias indicadas.

print("Clase 22 Ciclo for")
print()

# Declaramos algunas variables para el Ejemplo
sMensaje="Hola Mundo"

# Ciclo para acceder a cada una de las letras
for letra in sMensaje :
    print("Letra:",letra,"ascii:",ord(letra))
    print("-------------------")    
print()

# Objeto con Nombres
Empleados=("juan","pedro","alberto")

# Ciclo para acceder a cada uno de los nombres
for nombre in Empleados :
    print("Nombre:",nombre,"longitud:",len(nombre))
print()

# Verificando el Rango de una colección de Datos
print("Range:",range(len(sMensaje)))
print()

# Ciclo para acceder a cada una de las letras por indice
for indice in range(len(sMensaje)) :
    print("Letra:",sMensaje[indice],"ascii:",ord(sMensaje[indice]))
print()


# Verificando el Rango de una colección de Datos
print("Range:",range(len(Empleados)))
print()
# Ciclo para acceder a cada uno de los nombres
for indice in range(len(Empleados)) :
    print("Nombre:",Empleados[indice],"longitud:",len(Empleados[indice]))
    print(indice)
    print()
