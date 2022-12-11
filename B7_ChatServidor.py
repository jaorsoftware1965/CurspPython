# Clase 117
# Chat Servidor

# Importa la librería
import socket,threading

# Clase
class RecibeMensajes(threading.Thread):

    # Constructor
    def __init__(self,Socket,Origen):
        # Inicia el Hilo
        threading.Thread.__init__(self)
        
        # crea el socket para controlar
        self.socket = Socket
        
        # crea el origen
        self.origen = Origen
        
        # Daemon
        self.daemon=True;
                
    # El código que ejecutará el Hilo        
    def run(self):
        #mensaje
        print ("Escuchando Cliente desde:")
        print (self.origen[0],":",self.origen[1])

        try:                
        
            # Ciclo para  
            while True:  

                # Recibir datos
                recibido = self.socket.recv(100)  
                if recibido.decode("utf-8") == "salir":  
                    break        
                print()
                print (self.origen[0],":",self.origen[1],":",recibido.decode("utf-8"),"\n>",end="")
                
            # Sale  
            print ("Se ha cerrado la conexión con:",end="")
            print (self.origen[0],":",self.origen[1])
      
            # Cierra la conexión
            self.socket.close()              
            
        except (ConnectionAbortedError, ConnectionResetError) as err:       
            print("Se ha cerrado la conexión del Cliente")            
           

# Clase
class EnviaMensajes(threading.Thread):

    # Constructor
    def __init__(self,Socket):
        # Inicia el Hilo
        threading.Thread.__init__(self)
        
        # crea el socket para controlar
        self.socket = Socket
        
        # Daemon
        self.daemon=True;
                        
    # El código que ejecutará el Hilo        
    def run(self):
                
        # Ciclo para  
        while True:  
            # Solicita Mensaje a Enviar
            mensaje = input(">")
            if mensaje == "salir":  
                break        
            if mensaje != "":
               # envia el Mensaje
               self.socket.send(bytes(mensaje,'utf-8'))  
              
        # Cierra la conexión
        self.socket.close()                

# Crea un objeto de Sockets  
SocketServidor = socket.socket()   
print("Socket creado ...")

# Se conecta a un servidor a través de un puerto
SocketServidor.bind(("localhost", 9999))  
print("Se conecta a localhost por puerto 9999 ...")

# Se dispone a escuchar
SocketServidor.listen(1) # Solo una conexión  
print("Esperado Conexion ...")

# Acepta a un Cliente
SocketCliente, addr = SocketServidor.accept()  
print("Conexion aceptada desde:",addr[0],":",addr[1])

# Creo un objeto para Recibir Mensajes
xRecibeMensajes  = RecibeMensajes(SocketCliente,addr)

# Lanza el Hilo
xRecibeMensajes.start()

# Creo un objeto para Enviar Mensajes
xEnviaMensajes = EnviaMensajes(SocketCliente)

# Lanza el Hilo
xEnviaMensajes.start()

# Verifica que estén activos
while True:
    if (not xEnviaMensajes.is_alive() or   
        not xRecibeMensajes.is_alive()):
        break;
        
#Fin
print("Fin del Servidor")        
