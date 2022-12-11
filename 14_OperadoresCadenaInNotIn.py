# Clase 14 Operadores de Cadena in y not in

# En Clases anteriores vimos como podemos utilizar el operador [],*,+ para realizar operaciones
# con cadenas. En esta clase veremos 2 operadores mas que son: in y not in.
# Notemos que estos 2 operadores son parte de las palabras reservadas de Python
# El funcionamiento de estos 2 operadores es el siguiente

# -----------------------------------------------------------------------------------------------------
# Operador      Descripción                                Ejemplos considerando mensaje="Hola Mundo"
# -----------------------------------------------------------------------------------------------------
#    in         Si Existe en. Retorna True si si existe    "H" in mensaje = True
#    not it     No Existe en. Retorna True-si no existe    "H" not in mensaje = False

# Desplegamos Mensaje de la Clase
print("Clase 14 Operadores de Cadena in y not in")

# Declara variable con Mensaje
mensaje="Hola Mundo"

# Usa in y not in
print("h" in mensaje)
print("j" in mensaje)
print("holA" in mensaje)
print("hOla" not in mensaje)
