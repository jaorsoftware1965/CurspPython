# Clase 74 POO
# Propiedades Dinámicas

# Python cuenta con la posibilidad de agregar Propiedades dinámicamente

# Es decir, que despues de que se ha inicializado el Objeto, todavía es
# posible agregar propiedades adicionales

# Definimos una clase
class Alumno():
   
    # Propiedades del Alumno Públicas
    #Matricula  = ""
    #Nombre     = ""
    #Edad       = 0
    #Carrera    = ""	
    
    #Propiedad No publica
    #__MayorEdad  = False
        
    	
    # definimos el método para inicializar
    def __init__(self, Matricula, Nombre, Edad=32, Carrera="Informatica"):
        # Inicializamos las propiedades
        self.Matricula = Matricula
        self.Nombre    = Nombre
        self.Edad      = Edad
        self.Carrera   = Carrera
        if (self.Edad > 17):
            self.__MayorEdad=True
        else:
            self.__MayorEdad=False
        print ("Se ha Inicializado el Alumno")
				
	#Metodos
    def fnImprimirInformacion(self):
        print("Datos del Alumno")
        print("----------------")
        print("Matrícula :",self.Matricula)
        print("Nombre    :",self.Nombre)
        print("Edad      :",self.Edad)
        print("Carrera   :",self.Carrera)
        self.__fnImprimeMayorEdad()
        
    #Metodo no publico    
    def __fnImprimeMayorEdad(self):
        print("MayorEdad :",self.__MayorEdad)


# Creamos un objeto de la Clase Alumno
oAlumno = Alumno("M-12323","Marco Polo",14)

# Desplegamos su propiedades con dir
print (dir(oAlumno))
input()
print

# Agregamos Propiedades dinámicamente
oAlumno.Direccion = "Domicilio Conocido"
oAlumno.Telefono  = "123-34-89"

# Desplegamos su propiedades con dir
print (dir(oAlumno))
input()
print

# Imprimimos las propiedades dinámicas
print (oAlumno.Direccion)
print (oAlumno.Telefono)
input()

# Imprimimos la Informacion
oAlumno.fnImprimirInformacion()


