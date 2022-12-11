# Clase 92
# Generadores 2a Parte

# Ahora crearemos un generador que genera un número infinito de datos


# Definimos nuestra función
def paresInfinito():
    
    # Variable indice
    indice = 1
    
    # En este caso definimos un bucle infinito
    while True:
        # Devolvemos un valor con yield
        yield indice * 2
        indice = indice + 1


# variable para contar
contar = 0
    
print("Imprimimos los 10 primeros numeros pares")
    
# Para probarlo simplemente iteramos sobre la función
for numeroPar in paresInfinito():   
    
    # Imprime el Dato    
    print (numeroPar)
    
    # Incrementa el contador
    contar = contar +1
    
    #Verifica si ya llego a 10
    if (contar >= 10):
       # Sale del Ciclo si ya llego a 10
       break

#Detiene el Programa
input()
print()

#Inicializamos contar
contar=1

# Podemos llamar al Generador asignando a un objeto       
generadorPares = paresInfinito()

print("Imprimimos los 10 primeros numeros pares")

# Ciclo hasta 10
while contar <= 10:
      
      # Imprime el next del Generador
      print(next(generadorPares))    
      
      # Incrementa el contador
      contar = contar + 1

# Pausa el Programa      
input()
print()
 
# Infinito
print(next(generadorPares))    
print(next(generadorPares))    
print(next(generadorPares))    