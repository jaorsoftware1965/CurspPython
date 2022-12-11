# Clase 10 Operadores Asignación

# Al momento del curso, para los ejemplos que se han mostrado, hemos utilizado el operador de asignación
# que es el signo de igual (=).

# Existen otros operadores de asignación, que además de asignar un valor, realizan una operación previa.
# Las operaciones previas que realizan son las correspondientes a los operadores aritméticos.
# Estos operadores se utilizan para simplificar una operación en que la variable a la se le va a asignar
# un valor, su valor actual será utilizado en el valor a asignar. Ejemplo

# x = x + 1

# La anterior expresión en forma simplificada quedaría asi:
# x += 1

# A continuación cada uno de los operadores de asignación.

# -------------------------------------------------------------------------------------------------------
# Operador      Descripción                                         Ejemplo
# -------------------------------------------------------------------------------------------------------
#    =          Asigna el valor indicado a su derecha                   x  = 5;
#    +=         Asigna el valor con una suma previa                     x += 5; equivalente a: x = x + 5;
#    -=         Asigna el valor con una resta previa                    x -= 5; equivalente a: x = x - 5;
#    *=         Asigna el valor con una multiplicación previa           x *= 5; equivalente a: x = x * 5;
#    /=         Asigna el valor con una división previa                 x /= 5; equivalente a: x = x / 5;
#    %=         Asigna el valor con una operaciónd de módulo previa     x %= 5; equivalente a: x = x % 5;
#    **=        Asigna el valor con una operacion de exponente previa   x **= 5; equivalente a: x = x ** 5;
#    //=        Asigna el valor con una división entera previa          x //= 5; equivalente a: x = x // 5;


# Desplegamos Mensaje de la Clase
print("Clase 10 Operadores de Asignación")

# Declaro una variable y hacemos operacion
x = 10
x += 3
print ("x +=  3 = ", x)

# Asignamos de nuevo el valor de 10
x = 10
x -= 3
print ("x -=  3 = ", x)

# Asignamos de nuevo el valor de 10
x = 10
x *= 3
print ("x *=  3 = ", x)

# Asignamos de nuevo el valor de 10
x = 10
x /= 3
print ("x /=  3 = ", x)

# Asignamos de nuevo el valor de 10
x = 10
x %= 3
print ("x %=  3 = ", x)

# Asignamos de nuevo el valor de 10
x = 10
x //= 3
print ("x //=  3 = ", x)

# Asignamos de nuevo el valor de 10
x = 10
x **= 3
print ("x **=  3 = ", x)
