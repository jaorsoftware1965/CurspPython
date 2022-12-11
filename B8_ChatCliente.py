# Clase 118
# Chat Cliente

# Importa la librería
import socket,threading

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
            
        # Sale  
        print ("El cliente ha finalizado")
  
        # Cierra la conexión
        self.socket.close()                        
        
# Clase
class RecibeMensajes(threading.Thread):

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
        #mensaje
        try:                
            # Ciclo para  
            while True:  

                # Recibir datos
                recibido = self.socket.recv(100)  
                if recibido.decode("utf-8") == "salir":  
                    break        
                print()    
                print ("Servidor:",recibido.decode("utf-8"),"\n>",end="")
            
            # Sale  
            print ("Se ha cerrado la conexión con el Servidor:",end="")
  
            # Cierra la conexión
            self.socket.close()                      
            
        except (ConnectionAbortedError,ConnectionResetError) as err:       
            print("Se ha cerrado la conexión desde el Servidor")            
            
        

# Crea el Socket  
SocketServidor = socket.socket()   

# Se conecta al localhost
SocketServidor.connect(("localhost", 9999))  

# Crea un objeto para enviar Mensajes
xEnviaMensajes = EnviaMensajes(SocketServidor)
xEnviaMensajes.start()

# Crea un objeto para recibir mensajes
xRecibeMensajes = RecibeMensajes(SocketServidor)
xRecibeMensajes.start()

# Verifica que estén activos
while True:
    if (not xEnviaMensajes.is_alive() or   
        not xRecibeMensajes.is_alive()):
        break;
        
#Fin
print("Fin del Cliente")        
