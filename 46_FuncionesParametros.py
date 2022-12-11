# Clase 46 Funciones Parámetros

# En esta clase veremos en forma mas profunda lo que son los parámetros de una función.

# Un parámetro es algo que necesita una función para ejecutar sus instrucciones.
# Cuando se define una función se deben de estipular las cosas que necesita para funcionar.

# Por ejemplo si quiero definir una función que me devuelva el cuadrado de un numero, pues
# la función debe de tener establecido un parámetro donde reciba el número para obtener su cuadrado

# Las funciones pueden tener "n" parametros definidos, y al momento de llamar o utilizarlas se
# debe respetar el orden en que los parámetros fueron definidos, para su correcto funcionamiento

# Desplegamos Mensaje de la Clase
print ("Clase 46 Funciones Parámetros")
print ()

# Definimos una función desplegar un mensaje
def fnMensaje(sMensaje):
   "Imprime un mensaje en la pantalla"
   print (sMensaje)
   return

# Definimos una función para obtener el cuadrado de un  número
def fnIntCuadrado(iNumero):
   "Obtiene el Cuadrado de un Número y lo imprime"
   print (iNumero*iNumero)
   return (iNumero*iNumero)
   
# Definimos una función para multiplicar un numero por otro
def fnIntMultiplicar(iNumero1, iNumero2):
   "Multiplica un Número por Otro"
   return (iNumero1 * iNumero2)
   
# Definimos una función para desplegar un mensaje n veces
def fnMensajeN(sMensaje, Veces):
    for indice in range(Veces):
        print(sMensaje)
    
		
# Se llama a la función
fnMensaje ("Este es un Mensaje");
print()

# Llama a la función Cuadrado
print ("El cuadrado de 9 es")
fnIntCuadrado(9);
print()

# Utiliza el valor de retorno de la función cuadrado
print("El cuadrado de 9 es:",fnIntCuadrado(9))
print()

# Defino 2 variables
Num1=10
Num2=3
print("La mutiplicación de ",Num1," por ",Num2, " es:",fnIntMultiplicar(Num1,Num2));
print("Resultado de 5 x 6 :",fnIntMultiplicar(5,6))

# Imprimiendo el Mensaje 3 Veces
fnMensajeN("Hola",3);

#fnMensaje("Hola",3);
fnMensajeN("Hola")