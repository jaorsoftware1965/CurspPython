# Clase 109
# Insertando Multiples registros

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
    cursor.execute("SELECT * FROM usuarios")
    print("Consulta ejecutada ..")
    input()    
    
    # Lee todos los Registros
    registrosTodos = cursor.fetchall()
    
    # Ciclo para obtener cada registro
    for registro in registrosTodos:                       
        # Imprime        
        print(registro)
        
    # Pausa el terminar despliegue    
    input()
    
    usuarios = [('Javier','Perez','Javier Perez',2),
                ('Rodolfo','Mota','Rodolfo Mota',3)]
    
    # QUery para insertar
    sQuery = "INSERT INTO usuarios (nick,pass,name,rol)" \
             " VALUES (%s,%s,%s,%s)"
    
    # Executamos la Inserción Múltiple
    cursor.executemany(sQuery, usuarios)
    conexion.commit()
    print("Se han insertado los 2 registros")
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
        #Pausa    
        input()

    # Cerramos la conexión al Servidor    
    conexion.close() 
    print("Conexión cerrada ..")
    

# Captura del Error    
except mysql.connector.Error as err:  
    print(err)
    print(err.errno)
    print(err.msg)
