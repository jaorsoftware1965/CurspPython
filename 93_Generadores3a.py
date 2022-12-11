# Clase 93
# Generadores 3a Parte

# Ahora veremos un generador que devuelve 2 numeros
# Veremos un programa que genera los indices de una Matriz de n por m

def generaMatriz(renglones,columnas):

    # Variables
    indiceRen = 1
        
    # Ciclo
    while (indiceRen <= renglones):
    
        indiceCol = 1     
        while (indiceCol <= columnas):      
        
            # retorna los indices
            yield indiceRen, indiceCol
            indiceCol = indiceCol +1
        
        # Incrementa el contador
        indiceRen = indiceRen + 1        
   
# Genera los indices de una matriz por 4
gMatriz = generaMatriz(3,4)

# Ciclo para imprimir los indices de la Matriz
try:
    while True:
        print(next(gMatriz),end="")
        input()
   
except StopIteration:
   print("La iteración ha terminado")