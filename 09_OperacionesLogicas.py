# Clase 09 Operaciones Lógicas

# Los Operaciones Lógicas, son aquellas que sus operandos son valores booleanos y el resultado
# que devuelven tambien es un valor booleano.

# El Lenguaje Python realiza estas 3 Operciones Lógicas utilizando 3 palabras reservadas: and, or y not.

# A continuación se presentan las Tablas de Verdad de cada una de estas operaciones, las cuales se
# utilizan para identificar los resultados.

# -----------------------------------------------------
# Tabla and. Devuelve True únicamente si los 2 son True
# -----------------------------------------------------
# Op1       Op2      Op1 and Op2
# -----------------------------------------------------
# True      True        True
# True      False       False
# False     True        False
# False     False       False

# ------------------------------------------------------
# Tabla or. Devuelve False únicamente si los 2 son False
# ------------------------------------------------------
# Op1       Op2     Op1 or Op2
# ------------------------------------------------------
# True      True        True
# True      False       True
# False     True        True
# False     False       False

# -----------------------------------------------------
# Tabla not. Invierte el Valor del Operando
# -----------------------------------------------------
# Op1       not Op1
# -----------------------------------------------------
# True      False
# False     True


# Desplegamos Mensaje de la Clase
print("Clase 09 Operaciones Lógicas")

# Declaramos variables numéricas
a = True
b = False

# Accedemos a subconjunto de caracteres
print ("a and b      = ", a and b)
print ("b and b      = ", a and b)
print ("a or  b      = ", a or  b)
print ("b or  b      = ", b or  b)
print ("5 > 8 or  b  =" , 5 > 8 or b)
print ("5 < 8 and b  =" , 5 < 8 and b)
print ("not a        =", not a)
print ("not b        =", not b)

