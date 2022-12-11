# Clase 110
# Eliminando y Actualizando Registros

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
                                          
    # Creamos un Cursor para hacer consultas                                      
    cursor=conexion.cursor()
    
    # Ejecutamos una consulta
    cursor.execute("SELECT * FROM usuarios")
    
    # Lee todos los Registros
    registrosTodos = cursor.fetchall()
    
    print("Desplegando los Registros")
    # Ciclo para obtener cada registro
    for registro in registrosTodos:                       
        # Imprime        
        print(registro)
        
    # Pausa el terminar despliegue    
    reg = input("Capture el Registro Id a Eliminar :")

    # Preparando Query para Eliminar
    sQuery = "DELETE FROM usuarios WHERE id = %s"
        
    # Ejecutando
    cursor.execute(sQuery,(reg,))
    
    print("Sentencia Ejecutada ..")
    print("Registros Eliminados")
    print(cursor._rowcount)
    input()    
    conexion.commit()
    
    # Pausa el terminar despliegue    
    reg = input("Capture el Registro Id a Modificar Nombre :")
    nombre = input("Capture el Nombre :")

    # Preparando Query para Eliminar
    sQuery = "UPDATE usuarios set Name = %s WHERE id=%s"
        
    #Ejecutando la actulización
    cursor.execute(sQuery,(nombre,reg))
    
    print("Actualización Ejecutada ..")
    print("Registros Actualizados")
    print(cursor._rowcount)
    input()    
    conexion.commit()
    
    # Ejecutamos una consulta
    cursor.execute("SELECT * FROM usuarios")
    print("Desplegando Registros ...")
        
    while True:
        # Obteniendo 10 registros
        registros = cursor.fetchmany(10)
        
        # Verifico si no hubo registros
        if (not registros):
            # Sale si no hubo
            break
        
        # Ciclo para obtener no mas de 10 registros        
        for registro in registros:
            print(registro)

    # Cerramos la conexión al Servidor    
    conexion.close() 
    print("Conexión cerrada ..")
    

# Captura del Error    
except mysql.connector.Error as err:  
    print(err)
    print(err.errno)
    print(err.msg)
