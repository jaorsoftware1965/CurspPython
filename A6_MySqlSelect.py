# Clase 106
# Consultas con Select

# pip install mysql-connector
import mysql.connector

# Columnas en Tabla
COL_ID   = 0
COL_NICK = 1
COL_PASS = 2
COL_NAME = 3
COL_ROL  = 4


#Capturamos el Error
try:
    # Creamos una conexión
    conexion = mysql.connector.connect(host="localhost", 
                                       user="root", 
                                       passwd="",
                                       database="test")
                                      
    print("Conexión lograda ..")
    input()    
    
    # Creamos un Cursor para hacer consultas                                      
    cursor=conexion.cursor()
    print("Cursor creado ...")
    input()    
    
    # Ejecutamos una consulta
    cursor.execute("SELECT * FROM usuarios_noexiste")
    print("Consulta ejecutada ..")
    input()    
    
    # Ciclo para desplegar los datos obtenidos
    while True:
    
        # Lee el Registro
        registro = cursor.fetchone()
        print("Leyó un registro ..")
        input()    
        
        # Verifica si ya no hay nada
        if (registro is None):
           break
        
        # Imprime        
        print(registro)
        print(type(registro))
        print(registro[COL_ID],registro[COL_NICK],registro[COL_PASS],
              registro[COL_NAME],registro[COL_ROL])
        input()

    # Cerramos la conexión al Servidor    
    conexion.close() 
    print("Conexión cerrada ..")
    

# Captura del Error    
except mysql.connector.errors.InterfaceError:
    print ("No se logró la conexión al Servidor")
    
except mysql.connector.ProgrammingError:
    print ("Error en Consultas ")

    