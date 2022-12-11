# Clase 90
# Iteradores 2a

# En esta clase veremos como podemos implementar una Clase Iterador
# con los métodos __iter__ y __next__

# Desplegamos la Clase
print("Clase 90 Iteradores 2a")

# Definimos la clase Consecutivo
class Consecutivo:
  # Redefinimos el __iter__
  def __iter__(self):
    # Definimos una variable de Instancia
    self.contador = 0
    return self

  # Redefinimos el __next__
  def __next__(self):
    # Incrementamos el Contador
    self.contador += 1
    # Retornamos el Contador
    return self.contador

# Definimos un objeto de Consecutivo    
iterConsecutivo = Consecutivo()

# Obtenemos el Iterador
numero = iter(iterConsecutivo)

# Obtenemos el consecutivo
print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))
