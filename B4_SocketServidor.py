# Clase 114
# Sockets Servidor

# Importa la librería
import socket  

# Crea un objeto de Sockets  
SocketServidor = socket.socket()   
print("Socket creado ...")
print(SocketServidor)
input()

# Se conecta a un servidor a través de un puerto
SocketServidor.bind(("localhost", 9999))  
print("Se conecta a localhost por puerto 9999 ...")

# Se dispone a escuchar
SocketServidor.listen(1) # Solo una conexión  
print("Escuchando ...")

# Acepta a un Cliente
SocketCliente, addr = SocketServidor.accept()  
print(SocketCliente)
print(addr)
print("Aceptando ...")

 
# Ciclo para  
while True:  
    recibido = SocketCliente.recv(10)  
    if recibido.decode("utf-8") == "salir":  
        break        
    print ("Recibido:",recibido.decode("utf-8"))    
    
# Sale  
print ("El Servidor ha finalizado")
  
# Cierra el Cliente
SocketCliente.close()  

# Cierra el Servidor
SocketServidor.close()