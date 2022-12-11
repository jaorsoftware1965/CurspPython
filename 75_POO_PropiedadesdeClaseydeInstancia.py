# Clase 75 POO

# Propiedades de Clase y de Instancia

# Definimos una clase
class Alumno():
   
    # Propiedades que son únicas y son Compartidas por la Clase
    Universidad = "UNAM"
            	
    # definimos el método para inicializar
    def __init__(self, Matricula, Nombre, Edad=32, Carrera="Informatica"):
        # Inicializamos las propiedades que cada objeto crea
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
        print("Matrícula   :",self.Matricula)
        print("Nombre      :",self.Nombre)
        print("Edad        :",self.Edad)
        print("Carrera     :",self.Carrera)
        self.__fnImprimeMayorEdad()
        print("Universidad :",self.Universidad)
        
    #Metodo no publico    
    def __fnImprimeMayorEdad(self):
        print("MayorEdad   :",self.__MayorEdad)
        
    #Metodo para establecer la Universidad
    def fnUniversidadSet(self,universidad):
        self.Universidad=universidad
            

# Creamos un objeto de la Clase Alumno
oAlumno = Alumno("M-12323","Marco Polo")
# Imprimimos la Informacion
oAlumno.fnImprimirInformacion()
input()
print()

# Creamos un objeto de la Clase Alumno
oAlumno2 = Alumno("G-1277","Juan Escutia")
# Imprimimos la Informacion
oAlumno2.fnImprimirInformacion()
input()
print()

#Cambiamos la Universidad Usando la Clase
print("Cambianos la Universidad a través de la Clase")
Alumno.Universidad="UV"
input()
print()

# Imprimimos la Información de los 2 alumnos
oAlumno.fnImprimirInformacion()
input() 
print()

oAlumno2.fnImprimirInformacion()
input()
print()

#Cambiamos la Universidad a través del Alumno
print("Cambiamos a través del Alumno")
oAlumno.fnUniversidadSet("POLITECNICO")
input()
print()

# Imprimimos la Información de los 2 alumnos
oAlumno.fnImprimirInformacion()
input()
print()

oAlumno2.fnImprimirInformacion()
input()
print()

print("! La pregunta de los 64 mil pesos !")
print("¿ Como quedó la propiedad de clase ?");
input()
print()

print("Asi !")
print(Alumno.Universidad)
input()

Alumno.Universidad="ANAHUAC"

# Imprimimos la Información de los 2 alumnos
oAlumno.fnImprimirInformacion()
input()
print()

oAlumno2.fnImprimirInformacion()
input()
print()

print("¿ Que pasa si creo otro alumno ?")
oAlumno3 = Alumno("P-1555","Benito Juarez")
input()
print()

oAlumno3.fnImprimirInformacion()
input()
print()

print("! La Variable de Clase se mantendrá solo para los objetos que no han sido")
print("  modificados su universidad a través del objeto y para los nuevos que se generen !!")
print("! Una locura, ! No creeen !")
print()
input()

# Imprimimos la Información de los 2 alumnos
oAlumno.fnImprimirInformacion()
input()
print()











