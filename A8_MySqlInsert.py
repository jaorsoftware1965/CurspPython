# Clase 108
# Insertando registros

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
    
    #Solicita datos para grabar a la BD
    while True:
         
        # Solicita el Nick
        nick=input("Captura el Nick:")
         
        # Verifica que no esté vacío
        if (nick==""):
            break
    
        # Solicita los demás datos
        password = input("Captura el Password:")
        nombre   = input("Captura el Nombre:")
        rol      = input("Captura el Rol(1-5):")
    
        # Preparamos una Sentencia para Insertar
        sQuery = "INSERT INTO USUARIOS (nick,pass,name,rol)"
        sQuery = sQuery +" VALUES(%s,%s,%s,%s)"
    
        #En una tupla colocamos los valores
        valores = (nick,password,nombre,rol)
    
        # Insertamos un Registro en la tabla
        cursor.execute(sQuery, valores)
    
        #Mensaje
        print("Se ha insertado el registro")
        input()
        print()
        print()
        
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
        
        
        
    # Solicitamos confirmación        
    confirmar=input("Confirma la grabación de los Registros (S-N):")
    
    # Verifica confirmación
    if (confirmar=="S" or confirmar=="s"):
        # Ejecutamos commit
        conexion.commit()
        print("Se ha confirmado la transacción")
    else:  
        # Ejecutamos rollback
        conexion.rollback()
        print("Se ha cancelado la transacción")

    #Pausa        
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
