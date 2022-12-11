# Clase 103
# Archivos 10a
# Archivos Registro Acceso Secuencial

# Posicionamiento del Archivo
POS_INICIAL  = 0
POS_ACTUAL   = 1
POS_FINAL    = 2

#Definimos una clase Persona
class Persona:
    def __init__(self,nombre,edad,sexo,domicilio,telefono):
        self.nombre    = nombre
        self.edad      = edad
        self.sexo      = sexo
        self.domicilio = domicilio
        self.telefono  = telefono
    
    # Redefinimos el Método__str__    
    def __str__(self):
        # Construimos una cadena a retornar
        cadena=self.nombre+","+str(self.edad)+","+self.sexo
        cadena=cadena+","+self.domicilio+","+self.telefono
        return cadena
        
# Creamos un archivo para la información de las personas
aPersonas = open("Personas.dat", "a+")

# Variable para saber cuantos registros tiene un archivo
registros = 0

# Nos colocamos al inicio del archivo
aPersonas.seek(0,POS_INICIAL)

# Obtenemos cuantos registros tiene el archivo
while True:
   # Leemos una linea del archivo
   linea = aPersonas.readline()
   
   # Verificamos salida
   if (len(linea)==0):
       break
   
   #Incrementamos contador de registros    
   registros = registros + 1

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
        sexo      = input("Sexo:")
        domicilio = input("Domicilio:")
        telefono  = input("Telefono:")
        
        #Creamos el objeto con los datos obtenidos
        oPersona = Persona(nombre,edad,sexo,domicilio,telefono)
        
        #Lo imprimimos
        print ("Los datos a grabar son:")
        print (oPersona)
        input()
        
        # Vamos al final del Archivo
        #aPersonas.seek(0,POS_FINAL) no es necesario con modo "a"
        
        # Grabamos el registros
        aPersonas.write(str(oPersona)+"\n")
        
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
        aPersonas.seek(0,POS_INICIAL)
        
        # Renglon
        renglon = 1
        
        print ("Registros en el Archivo")
        
        # Ciclo para leer los registros
        for linea in aPersonas.readlines():
            print(renglon,">",linea,end="")
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
        
            # Renglon
            renglon = 1
            
            # Se posiciona al principio del Archivo
            aPersonas.seek(0,POS_INICIAL)
        
            # Ciclo para leer los registros
            for linea in aPersonas.readlines():
                if (renglon == regDesplegar):
                   print(renglon,">",linea,end="")
                   input()
                   break
                renglon=renglon+1   
           
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
        aPersonas.seek(0,POS_INICIAL)
        
        # Ciclo para leer los registros
        for linea in aPersonas.readlines():
            # Verifica si el registro contiene el criterio
            if (linea.find(criterio)>=0):
                print(renglon,">",linea,end="")               
            renglon=renglon+1   
                
        # Mensaje de finalizacion
        print()
        print("Busqueda finalizada")
        input()
       

#Mensaje de Salida
print()
print("El Programa ha finalizado ...")

# Close opend file
aPersonas.close()
