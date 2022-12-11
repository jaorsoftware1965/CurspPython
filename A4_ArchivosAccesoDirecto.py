# Clase 104
# Archivos 11a
# Archivos Registro Acceso Directo

# Importando os
import os.path

# Posicionamiento del Archivo
POS_INICIAL  = 0
POS_ACTUAL   = 1
POS_FINAL    = 2

# Función para ajustar una cadena a una longitud
def fnAjusta(cadena,longitud):

    #Verifica que la longitud de la cadena sea menor
    if (len(cadena)<longitud):        
        # Ajusta la longitud
        cadena = cadena.ljust(longitud," ")
    elif (len(cadena)>longitud) :
        cadena = cadena[0:longitud]
    
    # Retorna la cadena
    return cadena
                        
#Definimos una clase 
class Alumno:
    def __init__(self,nombre,edad,genero,domicilio,telefono):
        self.nombre      = fnAjusta(nombre,30)   
        self.edad        = fnAjusta(str(edad),2)
        self.genero      = fnAjusta(genero,1)
        self.domicilio   = fnAjusta(domicilio,30)
        self.telefono    = fnAjusta(telefono,15)
        self.cambioLinea = "\r\n"
        # Longitud del Registro 80
    
    # Redefinimos el Método__str__    
    def __str__(self):
        # Construimos una cadena a retornar
        cadena=self.nombre+str(self.edad)+self.genero
        cadena=cadena+self.domicilio+self.telefono
        cadena=cadena+self.cambioLinea
        return cadena

# Definimos la longitud del Registro
longitudRegistro = 80
        
# Verificar si existe el archivo
if (os.path.isfile("Alumnos.dat")):
   aAlumnos = open("Alumnos.dat", "rb+")
else:
   aAlumnos = open("Alumnos.dat", "wb+")

# Variable para saber cuantos registros tiene el archivo
registros = 0

# Obtenemos cuantos registros hay
aAlumnos.seek(0,POS_FINAL)
registros = aAlumnos.tell() / longitudRegistro


#Ciclo para el Menu
while True:
    # Despliega el numero de registros
    print ("Registros en el archivo:",registros)
    print ()

    print("Menu Principal")
    print("1.- Agregar")
    print("2.- Desplegar todos")
    print("3.- Desplegar un Registro")
    print("4.- Buscar")
    print("5.- Modificar")
    print("6.- Eliminar")
        
    opcion = input("Seleccione:")

    # Verifica opcion
    if (opcion==""):
        break
    
    # Verifica cada opcion
    if (opcion=="1"):
       
        #Agregar
        print("Capture los datos de la persona:")
        nombre    = input("Nombre:")
        edad      = input("Edad:")
        genero    = input("Genero:")
        domicilio = input("Domicilio:")
        telefono  = input("Telefono:")
        
        #Creamos el objeto con los datos obtenidos
        oAlumno = Alumno(nombre,edad,genero,domicilio,telefono)
        
        #Lo imprimimos
        print ("Los datos a grabar son:")
        print (oAlumno)
        input()
        
        # Vamos al final del Archivo
        aAlumnos.seek(0,POS_FINAL)
        
        # Grabamos el registro
        aAlumnos.write(bytes(str(oAlumno),'utf-8'))
                
        # Mensaje
        print("El Registro ha sido grabado")
        input()
        
        # Incrementamos el contador de registros
        registros = registros + 1
    
    # Verifica opcion de desplegar todos
    if (opcion=="2"):
        
        # Deja una Línea
        print()
        
        # Se posiciona al principio del Archivo
        aAlumnos.seek(0,POS_INICIAL)
        
        # Renglon
        renglon = 1
        
        print ("Registros en el Archivo")
        
        # Ciclo para leer los registros
        while True:        
            # Lee un Registro
            registro = aAlumnos.read(longitudRegistro)
            
            # Verifica longitud leida
            if (len(registro)==0):
                break
            
            print(renglon,">",registro)
            renglon=renglon+1    
        print()
        print("Se ha desplegado el archivo")
        input()
        
    # Verifica opcion de desplegar un registro
    if (opcion=="3"):
        
        # Solicita registro a desplegar
        regDesplegar = int(input("Cual registro desea desplegar:"))
                
        # Verifica que sea valido
        if (regDesplegar <=0 or regDesplegar > registros):
            #Mensaje de Error
            print("El Registro indicado no es correcto")
            input()
        else:
            # Mensaje
            print("Buscando registro:",regDesplegar,"...")
                    
            # Se posiciona en el registro
            posicion = (regDesplegar-1)*longitudRegistro
            aAlumnos.seek(posicion,POS_INICIAL)
            
            # Lee el registro
            registro = aAlumnos.read(longitudRegistro)
            
            # Imprime
            print(regDesplegar,">",registro)
            input()
        
           
    # Verifica opcion de Buscar
    if (opcion=="4"):  
       
        # Solicita el Criterio de Búsqueda
        criterio = input("Indique el criterio de Búsqueda:")
       
        # Mensaje
        print("Buscando registros ...")
        print()
        # Renglon
        renglon = 1
            
        # Se posiciona al principio del Archivo
        aAlumnos.seek(0,POS_INICIAL)
        
        # Ciclo para leer los registros
        while True:
            # lee el registro
            registro = aAlumnos.read(longitudRegistro)
            
            # Verifica que haya leido
            if (len(registro)==0):
               break            
            
            # Verifica si coincide con el criterio
            if (str(registro).find(criterio)>=0):
                print(renglon,">",registro)               
            # Incrementa el contador de renglon    
            renglon=renglon+1   
                
        # Mensaje de finalizacion
        print()
        print("Busqueda finalizada")
        input()
    
    # Verifica Modificar
    if (opcion=="5"):
        
        # Solicita registro a modificar
        regModificar = int(input("Cual registro desea Modificar:"))
                
        # Verifica que sea valido
        if (regModificar <=0 or regModificar > registros):
            #Mensaje de Error
            print("El Registro indicado no es correcto")
            input()
        else:
        
            # Capturo los datos nuevos
            print("Capture los NUEVOS datos de la persona:")
            nombre    = input("Nombre:")
            edad      = input("Edad:")
            genero    = input("Genero:")
            domicilio = input("Domicilio:")
            telefono  = input("Telefono:")
            
            #Creamos el objeto con los datos obtenidos
            oAlumno = Alumno(nombre,edad,genero,domicilio,telefono)
            
            #Lo imprimimos
            print ("Los datos a grabar son:")
            print (oAlumno)
            input()
        
            # Vamos a la posición del Registro a modificar
            posRegistro = (regModificar-1)*longitudRegistro
            aAlumnos.seek(posRegistro,POS_INICIAL)
        
            # Grabamos el registro
            aAlumnos.write(bytes(str(oAlumno),'utf-8'))
                
            # Mensaje
            print("El Registro ha sido modificado")
            input()
            
    # Verifica Eliminar
    if (opcion=="6"):
        
        # Solicita registro a eliminar
        regEliminar = int(input("Cual registro desea Eliminar:"))
                
        # Verifica que sea valido
        if (regEliminar <=0 or regEliminar > registros):
            #Mensaje de Error
            print("El Registro indicado no es correcto")
            input()
        else:
        
            # Creamos el objeto con datos vacios
            oAlumno = Alumno("","","","","")
            
            #Lo imprimimos
            print ("Los datos a grabar son:")
            print (oAlumno)
            input()
        
            # Vamos a la posición del Registro a modificar
            posRegistro = (regEliminar-1)*longitudRegistro
            aAlumnos.seek(posRegistro,POS_INICIAL)
        
            # Grabamos el registro
            aAlumnos.write(bytes(str(oAlumno),'utf-8'))
                
            # Mensaje
            print("El Registro ha sido Eliminado")
            input()  

#Mensaje de Salida
print()
print("El Programa ha finalizado ...")

# Close opend file
aAlumnos.close()
