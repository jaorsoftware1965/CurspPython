# Clase 72 POO
# Inicializando Objetos

# En Python existe un Método Especial llamado "__init__" el cual es utilizado
# para inicializar un objeto.

# Este método en otros lenguajes de programación es llamado el constructor.
# Este método se ejecuta en el Momento en que se crea un objeto de esa clase

# Inicializar un objeto, es simplemente darle valores iniciales a las propiedades
# y tal vez hasta ejecutar un proceso en específico. Esto no es tan común.

	   
# Definimos una clase Test
class Test():
    # definimos el método para inicializar
    def __init__(self):
        print ("Se ha creado un objeto Test")
		
# Definimos una clase
class Alumno():
    "Las clases tambien se documentan como las funciones y modulos"
    
    # Propiedades del Alumno
    Matricula  = ""
    Nombre     = ""
    Edad       = 0
    Carrera    = ""	
    MayorEdad  = False
    	
    # definimos el método para inicializar
    def __init__(self, Matricula, Nombre, Edad=32, Carrera="Informatica"):
        # Inicializamos las propiedades
        self.Matricula = Matricula
        self.Nombre    = Nombre
        self.Edad      = Edad
        self.Carrera   = Carrera
        if (self.Edad > 17):
            self.MayorEdad=True
            #MayorEdad=True
        print ("Se ha Inicializado el Alumno")
				
	#Metodos
    def fnImprimirInformacion(self):
        print("Datos del Alumno")
        print("----------------")
        print("Matrícula :",self.Matricula)
        print("Nombre    :",self.Nombre)
        print("Edad      :",self.Edad)
        print("Carrera   :",self.Carrera)
        print("MayorEdad :",self.MayorEdad)


# Creamos un objeto de Test
oTest = Test()
input()
		

# Creamos un objeto de la Clase Alumno
oAlumno = Alumno("M-12323","Marco Polo")

# Accedemos a un Método
oAlumno.fnImprimirInformacion()
input()
print()

# Creamos un objeto de la Clase Alumno
oAlumno2 = Alumno("M-44443","Benito Juárez",45)

# Accedemos a un Método
oAlumno2.fnImprimirInformacion()
input()
print()

# Creamos un objeto de la Clase Alumno
oAlumno3 = Alumno("M-122222","Juan Escutia",14,"Sistemas")

# Accedemos a un Método
oAlumno3.fnImprimirInformacion()
input()
print()
