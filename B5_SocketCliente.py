# Clase 115
# Socket Cliente

# Importa la librería
import socket  

# Crea el Socket  
SocketServidor = socket.socket()   

# Se conecta al localhost
SocketServidor.connect(("localhost", 9999))  

# Ciclo para mandar mensajes  
while True:  

      # Solicita mensaje a enviar
      mensaje = input("> ")  
      
      # Enviando el Mensaje
      SocketServidor.send(bytes(mensaje,'utf-8'))  
      
      # Si mensaje
      if (mensaje == "salir"):  
         break  
         
# Mensaje de salida del Cliente  
print ("El Cliente ha finalizado")

# Cierra el Socket  
SocketServidor.close()