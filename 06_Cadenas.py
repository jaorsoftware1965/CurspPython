# Clase 06 Cadenas

# Las Cadenas en Python, como en muchos lenguajes, es un conjunto de caracteres, los cuales se encuentran
# delimitados o "encerrados" entre comillas dobles("") o comillas simples('').
# nombre1 = "juan escutia"
# nombre2 = 'vicente guerrero'

# Se puede acceder a un subconjunto de los caracteres de un cadena utilizando el operador slice [] de la
# siguiente forma:
# nombre1[0]     Accede al primer caracter de la cadena; j
# nombre1[2:5]    Accede a partir de la posición 2 hasta antes del 5; cen

# La variables de tipo String en Python, permiten la concatenación de caracteres utilizando el operador "+"
# print (nombre1 + " Murió por la patria")

# Las variables de tipo String en Python permiten utilzar el operador "*" para hacer multiplicaciones de
# su contenido
# print (nombre1 * 2)   Imprirá el nombre1 2 veces; juan escutiajuan escutia

# Desplegamos Mensaje de la Clase
print("Clase 06 Cadenas")

# Declaramos variables de tipo cadena
nombre1 = "Juan Escutia"
nombre2 = 'Vicente Guerreo'

# Accedemos a subconjunto de caracteres
print ("La posición 0 del Nombre1:",nombre1[0])
print ("La posición 7 del Nombre2:",nombre2[7])
print ("La posición 2 al 6 del Nombre1:",nombre1[2:6])
print ("La posición 2 al 7 del Nombre2:",nombre2[2:7])
print ("El nombre1 * 5:",nombre1 * 5)
print ("El nombre2 + 'murio por la patria':",nombre2 + " murió por la patria")

