# Clase 35 Pilas y Colas

# En Clases anteriores vimos los Diversos Métodos que existen en el Manejo
# de Listas. Algunos de estos Métodos permiten en Python implementar fácilmente
# 2 de las Estructuras de Datos mas comunes que son las Pilas y las Colas (filas)

# Una Pila es una estructura de datos que sigue la lógica, por ejemplo; de crear una
# pila de Libros. Cada vez que se agrega un Libro a la Pila, este se agrega en la 
# parte superior de la Pila o Tope de la misma; y cada que vez que se necesite retirar 
# un libro de la Pila, se debe de retirar de la parte superior o tope.

# En Inglés esta estructura se conoce como LIFO; que corresponde a las siglas: Last
# In First Out; último en entrar es el primero en salir.

# Una Cola o Fila; es una estructura que sigue la lógica de una Cola o Fila de personas
# tratando de comprar Boletos para algún servicio. Esta lógica en Ingles se le conoce
# como FIFO; que significa First In First Out; primero en entrar es el primero en salir.

# Es posible implementar una Cola con Listas; adicionalmente Python tiene una clase
# especial para el manejo de ellas, que es parte del módulo collections y que se llama
# deque.

# A continuación veremos el ejemplo de como implementar tanto una Pila como una Cola.

# Importamos deque desde collections
from collections import deque

print("Clase 35 Pilas y Colas")
print()

# Creamos una Pila Vacía
pila = []

# Agregamos 3 Elementos a la Pila, con el Método append
# el cual agrega el elemento en el tope de la Pila
# Este método, en Estructura de datos para Pila se le conoce como PUSH
pila.append(10)
pila.append(5)
pila.append(19)
print("Pila:",pila)
print()

# Saca un elemento de la Pila; este método es conocido en Estructura de
# datos con el mismo nombre; POP
print("Sacamos un Elemento del Tope de la Pila:",pila.pop())
print(pila)
print()

# Las Pilas en Programación tienen diferentes usos; el mas simple y conocido
# es imprimir una cadena en orden Inverso; tal y como se observa en este Ejemplo

# Pila Vacía
pila = []

# Metemos un Mensaje a la Pila
pila.append("H")
pila.append("o")
pila.append("l")
pila.append("a")
pila.append(" ")
pila.append("M")
pila.append("u")
pila.append("n")
pila.append("d")
pila.append("o")

# Declaramos una variable para el Mensaje Inverso
sMensajeInverso = ""

# Ahora, para imprimir el mensaje al reverso solo sacamos los elementos de la Pila
# los colocamos en la variable mensaje e imprimos el Mensaje
while (len(pila)>0):
      sMensajeInverso += pila.pop()

#Imprimimos el Mensaje Inverso
print("Mensaje Inverso:",sMensajeInverso)      
print()
      

# Creamos una Cola Vacía
colaImpresion = []

# Agregamos Elementos a la Cola
colaImpresion.append("Manual.doc")
colaImpresion.append("Factura.txt")
colaImpresion.append("Reporte.dat")
print("Cola Impresión:",colaImpresion)
print()

# Para sacar o atender un elemento de la Cola de Impresión, usamos POP pero indicando 
# que sea el primer elemento que exista en la Cola de Impresión

# Ciclo del Servicio de Impresión para atender la Cola de Impresión
while (len(colaImpresion)>0):
      print("Imprimiendo:",colaImpresion.pop(0))
print("No hay mas elementos a Imprimir")      
print()

# Python tiene una clase especialmente dedica a las colas y se utiliza así_

# Creamos la Cola de Impresión
colaImpresion = deque()
print(type(colaImpresion))
print()

# Agregamos elementos a la Cola
colaImpresion.append("Manual.doc")
colaImpresion.append("Factura.txt")
colaImpresion.append("Reporte.dat")
print("Cola de Impresión:",colaImpresion)
print()

# Ciclo del Servicio de Impresión para atender la Cola de Impresión
while (len(colaImpresion)>0):
      print("Imprimiendo:",colaImpresion.popleft())
print("No hay mas elementos a Imprimir")      
print()