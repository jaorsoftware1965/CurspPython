# Clase 62 Paquetes 2a
# Alias, Control de Error y Ejecución de Modulos como Principal

# Al momento de importar un módulo, es posible asignarle un alias,
# el cual nos permitirá hacer referencia a el; de forma mas sencilla
# y reducida

# importamos de acuerdo al paquete
import pqFuncGrales.funcAritmeticas as m

# Desplegamos Mensaje de la Clase
print ("Clase 62 Paquetes 2a Alias")
print ()

# Hacemos uso de las Funciones de la librería
print ("Llamando a las Funciones en el Paquete-Módulo:");
print ("Factorial de 5:",m.factorial(5))
print ("Cuadrado  de 5:",m.cuadrado(5))
print ("Doble     de 5:",m.doble(5))
input()
print ()

print ("Llamando a las Variables del Módulo:");
print ("Sistema :",m.sistema)
print ("Version :",m.version)
input()
print ()

# Desplegamos el nombre del módulo
print("El nombre del Modulo")
print(m.__name__)
input()
print ()

print("El nombre del módulo principal")
print(__name__)	
input()
print ()
	
try:
    import empty2
except ImportError as e:
    print('Failed to import:', e)