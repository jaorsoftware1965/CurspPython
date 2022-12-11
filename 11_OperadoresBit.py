# Clase 11 Operadores de Bit

# Para poder entender estos operadores es indispensable conocer el Sistema Númerico Binario; ya que
# las operaciónes se realizan a nivel bit. Esto significa que los operandos son convertidos a binario
# y se realizan las operaciones entre los bits que representan a cada operando. Ejemplo

#  8 = 00001000       11110111 -9 en complemento a 2
# 15 = 00001111
#      --------
#      00000111

# Tambien es fundamental conocer la forma o el método que se utiliza para representar número negativos
# en binario; de los cuales se hará mencion del Método "complemento a 2".

# A continuación la tabla de los operadores a nivel bit que maneja Python

# -------------------------------------------------------------------------------------------------------
# Operador      Nombre       Descripción                                 Ejemplo           
# -------------------------------------------------------------------------------------------------------
#   &           And          Operación and entre bits de los operandos   x = 8 & 15; x vale  8
#   |           Or           Operación or  entre bits de los operandos   x = 8 & 15; x vale 15
#   ^           Xor          Operación xor entre bits de los operandos   x = 8 ^ 15; x vale  7
#   ~           Ca2          Operación de complemento a 2 del operando   x = ~8    ; x vale -9
#   <<          Left  Shift  Desplazamiento de bits a la izquierda       x = 8 << 2: x vale 32
#   >>          Right Shift  Desplazamiento de bits a la derecha         x = 8 >> 2: x vale  2


# Desplegamos Mensaje de la Clase
print("Clase 11 Operadores de Bit")

# Declaramos las variables
a = 8
b = 15

# Desplegamos las operaciones
print ("8 & 15 =  ", a & b)
print ("8 | 15 =  ", a | b)
print ("8 ^ 15 =  ", a ^ b)
print (" ~8    =  ", ~a)
print ("~~8    =  ", ~~a)
print ("8 << 2 =  ", a << 2)
print ("8 >> 2 =  ", a >> 2)
