# Clase 30 Listas Funciones

# Al igual que las Cadena y los Números, las Listas tambien tienen sus propias Funciones, 
# muchos de los cuales tienen un funcionamiento similar.

# A continuación veremos el uso de cada una de ellas.
# 

print("Clase 30 Listas Funciones")
print()

# Declaramos 2 listas para el Uso en los Ejemplo
list1 = ['Física', 'Química', 'Matemáticas']
list2 = list(range(5))

# Imprimimos las Listas
print("Listas de Ejemplo")
print(list1)
print(list2)
print()

print("Longitudes de las Listas")
print(len(list1))
print(len(list2))
print()

print("Máximos Elementos de las Listas")
print("Max elemento : ", max(list1))
print("Max elemento : ", max(list2))
print()

print("Mínimos Elementos de las Listas")
print("Min elemento : ", min(list1))
print("Min elemento : ", min(list2))
print()

# Tarea. Averiguar que devuelven las funcionas Max y Min si la Lista tiene elementos mezclados
# Contará 10 pts para el exámen que la puntuación mayor es de 10000  :) 

# Definimos un Tuple( Es el tema siguiente a las Listas)
aTuple =(123, 'C++', 'Java', 'Python')

# Convertimos a Lista
list3 = list(aTuple)
print("Lista generada del Tuple : ", list3)

# Definimos una Cadena
xCadena = "Hola Mundo"

# Convertimos a Lista
list4=list(xCadena)
print("Lista generada de la Cadena ", list4)
print()

# Agregar. Este Método agrega al Final. Si queremos insertar en un lugar especial
# podemos usar el recurso de la clase anterior
list1.append('Español')
print(list1)
# Agregar al Principio
list1[0:1]=["Programación",list1[0]]
print(list1)
# Reiniciamos la Lista a la Original
list1 = ['Física', 'Química', 'Matemáticas']
list1[0]=["Programación",list1[0]]
print(list1)
print()

# Reiniciamos la Lista a la Original
list1 = [10,'Física', 'Química', 'Matemáticas',10,34,"Física",10.0]
print(list1)

# Cuenta elementos
print("Count 10     : ", list1.count(10))
print("Count Física : ", list1.count('Física'))
print("Count física : ", list1.count('física'))
print()

# Nota. Esta Método genera un Error si no encuentra el elemento
# Busca Elementos
print('Index Química :', list1.index('Química'))
print('Index Física  :', list1.index('Física'))
print('Index 10      :', list1.index(10))
print('Index 10.0    :', list1.index(10.0))
print()

# Reiniciamos la Lista a la Original
list1 = ['Física', 'Química', 'Matemáticas']

# Insertando en un lugar específico
list1.insert(1, 'Biologia')
print('List1 : ', list1)
#list1.insert(-1, 'Biologia2') # No hace nada
print()

# Reiniciamos la Lista a la Original
list1 = ['Física', 'Química', 'Matemáticas']

# Extiende es similar a la operacion +
list1.extend(list2)
print('Extended List1 :', list1)
print()

# Reiniciamos la Lista a la Original
list1 = ['Física', 'Química', 'Matemáticas']

#Elimina un elemento del tope o el que se indique y lo devuelve
print(list1.pop())
print(list1)
print(list1.pop(0))
print(list1)
print()

# Reiniciamos la Lista 
list1 = ['Física', 'Matemáticas','Química', 'Matemáticas']

# Elimina elementos de la Lista. Error si no los encuentra
# Si el elemento existe mas de 1 vez, solo elimina el primero
list1.remove('Física')
print(list1)
list1.remove('Matemáticas')
print(list1)
print()

# Reiniciamos la Lista 
list1 = ['Física', 'Química', 'Matemáticas']

# Reverse. Invierte el orden de los elementos en la lista
list1.reverse()
print(list1)
print()

# Sort. Ordena los elementos que tienen que ser del mismo tipo
list1.sort()
print(list1)
print()
