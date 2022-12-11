# Clase 105
# Conexion a MySql

# pip install mysql-connector
import mysql.connector

#Capturamos el Error
try:
    # Creamos una conexión
    conexion1=mysql.connector.connect(host="localhost", 
                                      user="root", 
                                      passwd="")
                                      
    print("Conexión lograda ..")
    input()    
    
    # Creamos un Cursor para hacer consultas                                      
    cursor1=conexion1.cursor()
    print("Cursor creado ...")
    input()    
    
    # Ejecutamos una consulta
    cursor1.execute("show databases")
    print("Consulta ejecutada ..")
    input()    
    
    print("Desplegando bases de datos disponibles ..")
    
    # Ciclo para desplegar los datos obtenidos
    for base in cursor1:
        print(base)
        input()

    # Cerramos la conexión al Servidor    
    conexion1.close() 
    print("Conexión cerrada ..")
    

# Captura del Error    
except mysql.connector.errors.InterfaceError:
    print ("No se logró la conexión al Servidor")
