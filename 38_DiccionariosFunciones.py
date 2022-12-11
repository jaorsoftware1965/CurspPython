# Clase 38 Diccionarios Funciones

# Al igual que con todas las Estructura de Datos anteriormente estudiadas; los 
# Diccionarios también tienen sus propias Funciones.

# A continuación veremos cada una de ellas.

print("Clase 38 Diccionarios Funciones")
print()

# Definimos un Diccionario de Edades
dicEdades ={"juan":34, "Elsa":25, "Ramiro":45,"Juan":29}

# Imprimimos
print("Elementos del Diccionario:",len(dicEdades))
print()
print("Diccionario como cadena:",str(dicEdades))
print()

# Crear un diccionario a partir de una Secuencia
datos = ("Alberto","Gerardo","Elena")
dicEdades = dicEdades.fromkeys(datos)

# Los valores quedarán vacíos
print("Nuevo Diccionario:",dicEdades)

# Creamos un Diccionario a partir de la Tupla
dicEdades = dicEdades.fromkeys(datos,10)
print("Nuevo Diccionario:",dicEdades)

# Obtenemos el valor de una Llave y el valor default si no existe
print(dicEdades.get('Juan'))
print(dicEdades.get('Juan',"Sin definir"))
print()

# Agrega un Elemento al Diccionario con Su valor si no existe
# Devuelve el valor del Elemento
print(dicEdades.setdefault('Alberto', None))
print(dicEdades.setdefault('Juan', None))
print(dicEdades.setdefault('Martha',30))
print(dicEdades)
print()

# Agrega un Diccionario a otro
dicExtra = {"Eleuterio":30,"Israel":75,"Martha":34}
dicEdades.update(dicExtra)
print(dicEdades)
print()
