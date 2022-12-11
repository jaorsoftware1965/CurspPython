# Clase 13 Caracteres de Escape

# Los Caracteres de Escape, son un conjunto de Caracteres que tienen un significado o uso especial en la
# programación; siendo una de sus características principales, que no son imprimibles.
# Para ser representados o utilizados se hace uso del caracter BackSlash ("\").

# En la programación Batch en WIndows y Shell en Linux, son muy utilizados para controlar entre otras cosas
# la posición del Cursor y el Color en aplicaciones de Consola

# Estos caracteres, nos pemiten realizar acciones especiales; a continuación la tabla de los mas
# comunes y utilizados.

# ----------------------------------------------------------------
# Notación      Descripción                  
# ----------------------------------------------------------------
#    \\         BackSlash     
#    \'         Comilla Simple
#    \"         Comilla Doble
#    \b         BackSpace
#    \n         Nueva Linea
#    \r         0x0d                Retorno de Carro
#    \t         0x09                Tabulador


# Desplegamos Mensaje de la Clase
print("Clase 13 Caracteres de Escape")


# Probando las secuencias de escape
print("Imprimiendo el BackSlash \\ dentro de una cadena")
print("Imprimiendo \"Comillas Dobles\" dentro de una cadena")
print('Imprimiendo \'Comillas Simples\' dentro de una cadena')
print("Nueva Linea \n")
print("Retorno de Carro \rOtro Texto")
print("Tabulador \t Tabulador")
print("BackSpace\b\bBackSpace")
