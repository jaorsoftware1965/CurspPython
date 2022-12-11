# Clase 76 POO

# Apuntadores a Métodos
# Diferencia al hacer dir de un objeto y de la Clase
# Los Métodos en los objetos
# Las Funciones normales tambien puede referenciarse

    
# Definimos una clase
class MiClase:

    # Variable de Clase
    varDeClase=""
    
    # definimos el método para inicializar
    def __init__(self):
        self.varDeInstancia=10
       
    # Definimos una función   
    def fnSaludo(self):
        return 'hola mundo'
        
# Declaro un Objeto
oMiClase = MiClase()

# Diferencia entre el objeto y la clase
print(dir(oMiClase))
input()
print()
    
print(dir(MiClase))
input    
print()

# Ejecutando la Función de la Clase
cadenaSaludo = oMiClase.fnSaludo()
print (cadenaSaludo)
input()
print()

# Obteniendo la referencia a la Funcion
pFnSaludo = oMiClase.fnSaludo

# Imprimiendo la Función
print (pFnSaludo)
input()
print()

# Ejecutando la Función desde el Apuntador
otraCadenaSaludo = pFnSaludo()
print (otraCadenaSaludo)
input()
print()

# Definimos una función
def Test():
    print ("Mensaje desde Test")
    return("Test")

#Ejecutamos test
xCadena = Test()
input()
print()

print(xCadena)
input()
print()

#Obtenemos el apuntador    
pFn = Test
print(pFn)
input()

# Ejecutamos desde el Apuntador
xCadenaNueva = pFn()
input()
print()

print(xCadenaNueva)


