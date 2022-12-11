# Clase 34 Conjuntos Funciones Matemáticas y de Dimensión

# Al igual que con las Listas y las Tuplas; los Conjuntos tambien tienen sus propias
# funciones las cuales veremos a continuación. 
# 
# En esta clase veremos las Funciones Matemáticas que están disponibles para los 
# conjuntos y que algunas son similares a los operadores vistos en clase anterior.

# Tambien veremos funciones que nos permiten modificar el número de elementos del
# Conjunto

# A continuación veremos los ejemplos de su uso

print("Clase 34 Conjuntos Funciones Matemáticas y de Dimensión")
print()

# Creamos 4 conjuntos
base10      = {0,1,2,3,4,5,6,7,8,9}
base8       = {0,1,2,3,4,5,6,7}
base2       = {0,1}
base16      = {0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E"}
vocales     = {"a","e","i","o","u"}


print("Funciones Matemáticas")
print()

print("union  :",vocales.union(base2))
print(vocales)
vocales.update(base2)
print(vocales)
vocales = {"a","e","i","o","u"} 
print()


print("diferencia :",base10.difference(base8))
print(base10)
base10.difference_update(base8)
print(base10)
base10 = {0,1,2,3,4,5,6,7,8,9}
print()

print("intersección :",base8.intersection(base2))
print(base8)
base8.intersection_update(base2)
print(base8)
base8 = {0,1,2,3,4,5,6,7}
print()

print("diferencia simétrica       :",base16.symmetric_difference(base8))
print(base16)
base16.symmetric_difference_update(base8)
print(base16)
base16 = {0,1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E"}
print()

# Devuelve true si tienen un intersección vacía
print("Intersección vacía:",base10.isdisjoint(base16))
print("Intersección vacía:",base10.isdisjoint(vocales))
print()

print("SubConjunto:",base10.issubset(base16))
print("SubConjunto:",base16.issubset(base10))
print("SubConjunto:",vocales.issubset(base10))
print()

print("SuperConjunto:",base10.issuperset(base16))
print("SuperConjunto:",base16.issuperset(base10))
print("SuperConjunto:",vocales.issuperset(base10))
print()

# Agrega un Elemento
vocales.add("z")
print("add    :",vocales)
vocales.discard("z")
print("discard:",vocales)
vocales.pop()
print("pop:",vocales)
vocales.remove("a") # Si no existe el elemento marca error
print("remove:",vocales)
print("len:",len(vocales))
vocales.clear()
print("clear:",vocales)
print("len:",len(vocales))