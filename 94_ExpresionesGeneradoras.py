# Clase 94
# Expresiones Generadoras

# Una expresión generadora, tal y como nos lo indica el concepto, nos
# permite generar datos en base a una expresion

# Imprimimos una expresion generadora
print("Imprimimos la expresión generadora")
print (i for i in range(3))
input()
print()

# Obtenemos los datos asignandolos a una variable
print("Imprimimos como lista")
x = (i for i in range(3))

# Imprimimos como lista
print(list(x))
input()
print()

# Obtenemos de nuevo los datos porque ya se consumieron
x = (i for i in range(3))

# Imprimimos los valores uno por uno
print("Imprimimos los valores uno por uno")
try:
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print("Se ha alcanzado el final de los datos")           
input()
print()
    
# Obtenemos los datos
x = (i**2 for i in range(3))
    
# Imprimimos como lista
print("Imprimimos la lista")
print(list(x))
input()
print()

# Obtenemos los datos
x = (i**2 for i in range(3))

print("Imprimimos los valores uno por uno")
# Imprimimos los valores uno por uno
try:
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print("Se ha alcanzado el final de los datos")           
input()
print()
    
# Creamos una expresión generadora con letras    
x = (i for i in 'abc')   

# Imprimimos como lista
print("Imprimimos como lista")
print(list(x))
input()
print()

# Creamos una expresión generadora con letras    
x = (i for i in "abc")   
print("Imprimimos uno por uno con su ordinal")
try:
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
except StopIteration:
    print("Se ha alcanzado el final de los datos")           
input()
print()

# Creamos un diccionario con la expresión generadora
diccionario = dict((i,ord(i)) for i in 'abc')
print("Imprimimos el Diccionario")
print(diccionario)
input()
print()

# Ejecutamos una suma en bases a los elementos generados
print("Imprimimos la Lista")
print (list(i*2 for i in range(5)))
input()
print()

print("Imprimimos una suma a partir de la expresión generadora")
print (sum(i*2 for i in range(5)))
