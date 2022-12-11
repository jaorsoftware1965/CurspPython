# Clase 89
# Iteradores

# Un iterador es un objeto que permite acceder a cada uno de los objetos
# de una colección sin importar su implementación

# Para realizar esto hace uso de algo llamado "protocolo iterador" el cual
# consiste de 2 métodos

# El método iter el cual retorna el objeto y el metodo next el cual
# obtiene el siguiente elemento de la colección

# Desplegamos la Clase
print("Clase 89 Iteradores")

# Definimos una colección de datos
cadena = "Esta es una colección de datos"

# Ejecutamos un ciclo para obtener cada elemento
print("Impresión con un ciclo for tradicional");
for letra in cadena:
   print(letra, end="")

# Espacio   
print()
input()

# Ahora usando un iterador
itCadena = iter(cadena)

# Obtenemos la longitud de la Cadena
longitud = (len(cadena))

# Imprimimos cada elemento de la Cadena
print("Impresión con un iterador");
while (longitud > 0) :
     print(itCadena.__next__(),end="")
     longitud = longitud - 1
print()
input()

# Ahora usando un iterador
itCadena = iter(cadena)

# Obtenemos la longitud de la Cadena
longitud = (len(cadena))

# Imprimimos cada elemento de la Cadena
print("Impresión con un interador 2");
while (longitud > 5) :
     print(next(itCadena), end="")
     longitud = longitud - 1
print()
input()


# Imprimimos como una lista, y solo los restantes
# itCadena = iter(cadena)
print("Impresión como una lista");
print(list(itCadena))
input()

try:
    # Tratamos de obtener un elemento cuando ya no hay
    print(next(itCadena), end="")
except StopIteration:
    print("Se ha alcanzado el final de la lista")       
input()    

# Declaramos una lista  
lista = [10, 100, 1000, 10000]
iterador = iter(lista)
try:
    while True:
        print(iterador.__next__())        

except StopIteration:
    print("Se ha alcanzado el final de la lista")   