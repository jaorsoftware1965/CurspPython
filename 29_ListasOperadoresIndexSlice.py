# Clase 29 Listas Operadores Indexamiento y Slice

# En esta Clase veremos que operadores, algunos de los que ya hemos visto; pueden ser utilizados on
# Listas, así como ejemplos de Indexamiento y de Slice.
# 
# En las Listas, se pueden usar los operadores * y +, tal y como se usaron en las Cadenas; solo que en
# este caso el resultado que devolverán será una Lista y no una Cadena. A continuación se muestra la tabla 
# con ejemplos al respecto.

# -----------------------------------------------------------------------------------------------
#   Expresión en Python                 Resultado                           Operación
# -----------------------------------------------------------------------------------------------
#   [21, 32, 53] + [14, 15, 16]	        [21, 32, 53, 14, 15, 16]	        Concatenacion
#   ['123'] * 4	                        ['123', '123', '123', '12']	        Repetición
#   33 in [11, 22, 33]	                True	                            Inclusión/Pertenencia
 
# El acceso a través de Índices (Indexamiento), como lo hemos visto anteriormente, es posible. Acá
# algunos ejemplos adicionales; uno de ellos es el indexamiento negativo.

# Considerando que:
# L = ['C++'', 'Java', 'Python']

# ---------------------------------------------------------------------------------------------------------
#   Expresión en Python                 Resultado                 Descripción
# ---------------------------------------------------------------------------------------------------------
#   L[2]	                            'Python'	              Desplazamiento desde 0
#   L[-2]	                            'Java'	                  Conteo negativo desde la Derecha desde -1
#   L[1:]	                            ['Java', 'Python']	      Rangos Intervalos
#

print("Clase 29 Listas Operadores Indexamiento y Slices")
print()


# Declaramos 3 listas
mezclados = ['Python', 'Java', 1997, 2000]
edades    = [15, 12, 23, 14, 55 ]
vocales   = ["a","e","i","o","u"]

# Operaciones con Listas
print("Operaciones con Listas")
print(mezclados + [12.3,24.5])
print(mezclados + edades)
print(vocales * 2)
print(edades * 2)
print(15 in edades)
print()

print("Indexamientos")
print(mezclados)
print(mezclados[2])
print(mezclados[-1])
print(mezclados[2:])
print(mezclados[-3:])
print()

# Indexamiento Posivito y Negativo en Cadenas
sMensaje ="Hola Mundo"
print("sMensaje    :",sMensaje)
print("sMensaje[3] :",sMensaje[3])
print("sMensaje[-3];",sMensaje[-3])



