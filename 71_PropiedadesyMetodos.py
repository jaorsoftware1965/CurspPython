# Clase 71 POO
# Estableciendo Propiedades y Métodos en una Clase

# Definimos una clase
class Alumno():
    
	# Propiedades del Alumno
    Matricula  = "CI-102018"
    Nombre     = "Juan Perez"
    Edad       = 22
    Carrera    = "Informatica"	
    
	# Metodo que solo despliega un Mensaje
    def fnTest(self):
	    print ("Función fnTest")

		
	#Metodos
    def fnImprimirInformacion(self):
        print("Datos del Alumno")
        print("----------------")
        print(self.Matricula)
        print(self.Nombre)
        print(self.Edad)
        print(self.Carrera)

	# Metodo para Establecer la Carrera
    def fnSetCarrera(self,Carrera):
        self.Carrera = Carrera


# Creamos un objeto de la Clase Alumno
oAlumno = Alumno()

# Accedemos a la propiedad
print("Matricula del Alumno:")
print(oAlumno.Matricula)
input()
print()

# Accedemos a un Métodos
oAlumno.fnImprimirInformacion()
input()
print()


#Accedemos a la otra funcion
oAlumno.fnTest
input()
print()

#Cambiamos la Carrera
oAlumno.fnSetCarrera("Sistemas")

# Accedemos a un Métodos
oAlumno.fnImprimirInformacion()
input()
print()

print(dir(oAlumno))

