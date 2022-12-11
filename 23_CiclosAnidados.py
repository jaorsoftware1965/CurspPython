# Clase 23 Ciclos Anidados

# Tal y como se explicó en la sentencia if, también es posible tener Ciclos anidados; es decir; ciclos 
# dentro de Ciclos. 

# A continuación ejemplos al respecto

print("Clase 23 Ciclos Anidados")
print()

# Declaramos algunas variables para el Ejemplo
tabla = 1
multiplicador = 1

# Ciclos anidados para presentar las tablas de Multiplicar del 1 al 5
# mutiplicando del 1 hasta el 10
while (tabla <= 5) :
    #Mensaje de la tabla a imprimir
    print("Tabla del ",tabla)
    print("------------")
    while (multiplicador <=10) :
        # Imprimo la Multiplicación
        print(tabla,"X",multiplicador,"=",tabla*multiplicador)
        # Incremento el Multiplicador
        multiplicador += 1
    else :
        # Dejo una linea en blanco
        print()
    # Inicializo el Multiplicador
    multiplicador = 1
    # Incremento la Tabla
    tabla += 1
else:
    print("Fin de impresión de Tablas con while")        
    print()


# Ciclo para imprimir las tablas con for
for tabla in range(5,11):
    print("Tabla del ",tabla)
    print("------------")
    for multiplicador in range(1,11):
        # Imprimo la Multiplicación
        print(tabla,"X",multiplicador,"=",tabla*multiplicador)
    # Dejo una linea en blanco
    print()
else:
    print("Fin de impresión de Tablas con for")        
    print()
        