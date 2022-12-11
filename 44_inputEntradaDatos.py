# Clase 44 input Entrada de datos

# En esta clase veremos como Python nos permite capturar datos desde el teclado
# y almacenarlos en variables, para lo cual haremos uso de la función input

# La función input nos permite desplegar un mensaje, el cual es opcional; para
# que el usuario capture lo que desee con el teclado y lo almacene en una variable;
# lo cual tambien es opcional.



# Desplegamos Mensaje de la Clase
print ("Clase 44 input Entrada de Datos")
print ()

# Capturando datos sin almacenar la informacion
input ("Escriba lo que desee y presione Enter para Finalizar:")
print ()

# Capturando datos y asignandolo a una variable
xDato = input ("Escriba lo que desee y presione Enter para Finalizar:")

# Despliega lo capturado
print ("Capturado:",xDato)
print ()

# Mensaje de captura
print ("Capture lo que desee:")

# Capturando sin mensaje
xDato = input()
print ("Capturado:",xDato)
print ()

# Solicita la captura de un Número
Edad = input("Capture su edad:")

# Verifica que haya capturado un integer
if (Edad.isnumeric()):
   # Convirtiendo a Entero
   Edad = int(Edad)
   print ("Su edad es:",Edad)
else:
   print ("Error: no capturaste un Numero para la Edad")
print ()

# Solicita la captura de un Número
Peso = input("Capture su Peso:")
Peso = float(Peso)
print ("Su Peso es:",Peso)
print ()

# Capturando y Convirtiendo al mismo tiempo
Nombre = input ("Capture su Nombre:")
Edad   = int(input("Capture se Edad:"))
Peso   = float(input("Capture se Peso:"))
print()

print("Tipo de Nombre:",type(Nombre))
print("Tipo de Edad  :",type(Edad))
print("Tipo de Peso  :",type(Peso))

