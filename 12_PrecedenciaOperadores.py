# Clase 12 Precedencia de Operadores

# En Programación se conoce como Precedencia de operadores, al orden en que se ejecutan las diversas
# operaciones que puede haber en una expresión.

# Se dice que un Operador tiene mayor precedencia que otro, cuando los 2 se encuentran en una expresión
# pero uno se tiene que ejecutar primero que el otro.

# La forma natural de evaluar una expresión, es de izquierda a derecha; pero en caso de que el operador
# que esté a la derecha, tenga mayor precedencia que el anterior; este deberá de ejecutarse primero.

# En la expresión: 5 + 4 * 2; quien no conozca la precedencia de operadores; dirá que el resultado de la
# expresión es 18; porque primero sumara 5 + 4 = 9; y posteriormente multiplicará 9 * 2; dando como 
# resultado 18; el cual es incorrecto; porque la multiplicación tiene mayor precedencia que la suma, por
# lo que primero deberá de multiplicar 4 * 2 = 8; y posteriormente sumar 5 + 8 = 13; siendo este el 
# resultado correcto.

# Cuando los operadores tienen la misma precedencia se evalua de izquierda a derecha; a menos que haya
# paréntesis; que obliguen a realizar una operación antes que otra.
# Para el ejemplo indicado, si se quisiera realizar la suma antes de la multiplicación, la expresión
# tendría que escribirse de la siguiente forma: (5 + 4) * 2

# A continuación se muestra la precedencia de operadores. Los que se encuentran arriba tienen mayor
# precedencia que los que se encuentra debajo.

# -----------------------------------------------------------------------------------------------
# Operadores                    Operadores/Operaciones
# -----------------------------------------------------------------------------------------------
#   ()                          Parentesis
#   **                          Exponenciación
#   ~, +, -                     Complemento; suma y resta con un operando (unaria)
#   *, /, %, //, @              Multiplicación, División, Módulo, División Entera, Mult Matrices
#   +,-                         Suma y Resta con dos operandos (binaria)  
#   <<, >>                      Left y Right Shift (Desplazamientos)
#   &                           Operación de Bit And
#   ^                           Operacion de Bit Xor
#   |                           Operación de Bit Or
# <=, <, >, >=, ==, !=,         Operadores de Comparación,Operaciones de Identididad
# in, not in, is, is not        
# = %= /= //= -= += *= **=      Operadores de Asignación
# not                           Operaciones Lógica not
# and                           Operaciones Lógica and
# or                            Operaciones Lógica or


# Ejemplos

# 5 + 6 / 2 * 4
# 5 +   3   * 4
# 5 +       12
#   17

# (5 + 6) * 8 / 4 + 2
#    11   * 8 / 4 + 2
#         88  / 4 + 2
#             22  + 2
#                 24

# 5 * 2 ** 3
# 5 * 8
#   40

# False and True or False
#       False    or False
#                False

# False or True and True
# False or      True
#       True

# False and not True or False
# False and False    or False
#       False        or False
#                    False

# not False and True or not True
# True      and True or False
#           True     or False
#                    True

# 5 | 8 ^ 10 & 4                        10 = 1010   8 = 1000   5 = 0101
# 5 | 8 ^    0                           4 = 0100   0 = 0000   8 = 1000
# 5 |   8                               ---------   --------   --------
#   13                                   & = 0000   ^ = 1000   | = 1101


# Desplegamos Mensaje de la Clase
print("Clase 12 Precedencia de Operadores")


# Precedencia de Operaciones Artiméticas
print(5 + 6 / 2 * 4)         # 17
print((5 + 6) * 8 / 4 + 2)   # 24
print(5 * 2 ** 3 )           # 40

# Precednecia de Operaciones Lógicas
print (False and True or  False)          # False
print (False or  True and True)           # True
print (False and not True or False)       # False
print (not False and True or not True)    # True

# Precedencia de Operaciones de Bit
print(5 | 8 ^ 10 & 4)
           