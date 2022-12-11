# Clase 48 Funciones Parámetros Múltiples

# En esta clase veremos como es posible poder definir y utilizar funciones con un número
# de parámetros indefinido; es decir; múltiples

# Desplegamos Mensaje de la Clase
print ("Clase 48 Funciones Parámetros Múltiples")
print ()


def fnMyPrint(* datos):
    "Imprime n datos por la pantalla"
    print (datos)
    print (type(datos))
    for xdato in datos:  # recorre, uno a uno
        print (xdato,end=" ")
    print()	
    

# Llama a la función
variable = 45
fnMyPrint("Hola",variable,5,6,'a')


def fnMyPrint2(fijo, * datos):
    "Imprime n datos por la pantalla"
    for xdato in datos:  # recorre, uno a uno
        print (xdato,end=" ")
    print(fijo);	
    

# Llama a la función
variable = 23
fnMyPrint2("Saludos",variable,5,6,'a')

# Definimos una función desplegar un mensaje
def fnMyPrint3(fijo, * datos, fijo2=77):
    "Imprime n datos por la pantalla"
    for xdato in datos:  # recorre, uno a uno
        print (xdato,end=" ")
    print(fijo)	
    print(fijo2)
	

# Llama a la función
variable = 56
fnMyPrint3("Que tal",variable,5,6,'a',89)