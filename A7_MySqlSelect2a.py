# Clase 107
# Consultas con Select 2a

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
    
    # Lee todos los Registros
    registrosTodos = cursor.fetchall()
    
    # Ciclo para obtener cada registro
    for registro in registrosTodos:        
        print("obtuvo un registro ..")
        input()    
                
        # Imprime        
        print(registro)
        print(type(registro))
        print(registro[COL_ID],registro[COL_NICK],registro[COL_PASS],
              registro[COL_NAME],registro[COL_ROL])
        input()
        
    #Ejecutando de nuevo otra consulta    
    cursor.execute("SELECT * FROM usuarios")
    print("Consulta ejecutada ..")
    input()    
    
    while True:
        print("Obteniendo 10 registros ...")
        registros = cursor.fetchmany(10)
        
        # Verifico si no hubo registros
        if (not registros):
            # Sale si no hubo
            break
        
        # Ciclo para obtener no mas de 10 registros        
        for registro in registros:
            print(registro)
            print(type(registro))
            print(registro[COL_ID],registro[COL_NICK],registro[COL_PASS],
                  registro[COL_NAME],registro[COL_ROL])
            input()

    # Cerramos la conexión al Servidor    
    conexion.close() 
    print("Conexión cerrada ..")
    

# Captura del Error    
except mysql.connector.Error as err:  
    print(err)
