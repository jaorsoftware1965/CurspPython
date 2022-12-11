# Clase 73 POO

# Propiedades y Funciones No Publicas

# Python maneja 2 de tipos de Propiedades y Métodos que son los siguientes:

# publica. Que pueden ser accedidas desde la clase, clase heredada u objeto
# no publica. Que pueden ser accedidas unicamente desde la clase

# Para indicar que una propiedad o función es no publica, Python no lo hace como
# otros lenguajes de programación, a través de una palabra reservada; sino
# que lo hace a través del nombre de la función.

# Si la propiedad o función inicia con "__" entonces es no publica

# Nota. Mencionar Atributo

# Definimos una clase
class Alumno():
   
    # Propiedades del Alumno Públicas
    Matricula  = ""
    Nombre     = ""
    Edad       = 0
    Carrera    = ""	
    
    #Propiedad No publica
    __MayorEdad  = False
        
    	
    # definimos el método para inicializar
    def __init__(self, Matricula, Nombre, Edad=32, Carrera="Informatica"):
        # Inicializamos las propiedades
        self.Matricula = Matricula
        self.Nombre    = Nombre
        self.Edad      = Edad
        self.Carrera   = Carrera
        if (self.Edad > 17):
            self.__MayorEdad=True
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
oAlumno = Alumno("M-12323","Marco Polo")

# Desplegamos su propiedades con dir
print (dir(oAlumno))
input()
print

# Accedemos a un Método
oAlumno.fnImprimirInformacion()
input()
print()

# No puedo acceder a su propiedad no publica
#print (oAlumno.__MayorEdad)

#No puedo acceder a su método no publico
#oAlumno.__fnImprimeMayorEdad()

