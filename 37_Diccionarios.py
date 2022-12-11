# Clase 37 Diccionarios

# En esta clase veremos otra Estructura de Datos que son los Diccionarios.
# Los Diccionarios de Datos, son colecciones de datos que a diferencia de las
# anteriores vistas, no se indexan a través de un índice numérico; sino que lo
# hacen a través de Keys's (Claves). En php hay una forma muy parecida de realizarlo.

# Las Claves pueden ser cadenas, números, y tuplas; siempre y cuando estas contengan
# cadenas o números. No es posible usar Listas como Claves de Diccionarios.

# La manera mas simple de entender un diccinario, es verlo como un conjunto no
# ordenado de pares de datos; en donde el primer dato es la clave y el segundo dato
# es el valor de la clave; con el requerimiento de que las claves deben ser ÚNICAS;
# es decir que no puede haber llaves repetidas.

# Los símbolos utilizados para definir un Diccionario, son las {}'s. Un par de llaves
# sin información crean un diccionario vacío. Ejemplo:

# dicVacio = {}

# Las Claves y el Valor de un diccionario, son separados por ":" y cada elemento del 
# diccionario es separado por ",". Ejemplo:

# dicEdades ={"juan":34, "Elsa":25, "Ramiro":45}

# Las Operaciones Base de un Diccionario son la de colocar un valor para una clave, y
# obtener el valor de una clave. Para hacer referencia a la Clave, se utilizan "[]".
# Ejemplo

# dicEdades['juan']=45

# Veremos como con la instrucción "del" (palabra reservada), podemos eliminar un elemento
# del diccionario; e inclusive toda la variable para que ya no exista mas.
# La palabra reservada "del" es posible utilizarla con CUALQUIER otra variable definida.
# Su función es eliminar de memoria la variable sin importar su tipo.

print("Clase 37 Diccionarios")
print()

# Creamos el Diccionario Vacío
dicVacio = {}
# Imprimimos el Tipo
print(type(dicVacio))
print()

# Definimos un Diccionario de Edades
dicEdades ={"juan":34, "Elsa":25, "Ramiro":45,"Juan":29}

# Imprimimos
print(dicEdades)
#print(dicEdades['Juan']) # Es sensible al texto, marca error
print(dicEdades['juan'])
print(dicEdades['Elsa'])
#print(dicEdades[1:2]) # No se puede hacer slice
print(dicEdades.keys())
print(dicEdades.values())
print(dicEdades.items())
print()

# Actualizando los datos
dicEdades['juan']=45
print(dicEdades['juan'])
dicEdades['Elsa']="Mayor"
print(dicEdades['Elsa']) # Actualizamos cambiando el tipo de dato del Valor
print()

# Ciclo para navegar en cada llave
for xDato in dicEdades.keys():
    print("Key:",xDato)
print()

# Ciclo para navegar en cada valor
for xDato in dicEdades.values():
    print("Value:",xDato)
print()

# Ciclo para navegar en cada item
for xKey, xVal in dicEdades.items():
    print("Key:",xKey, "Val:",xVal)
print()

# Eliminando Elementos del Diccionario
del dicEdades['Ramiro']
print(dicEdades)
print()

# Eliminamos todos los Elementos
dicEdades.clear()
print(dicEdades)
print()

# Eliminamos la variable
del dicEdades
#print(dicEdades) # NameError: name 'dicEdades' is not defined