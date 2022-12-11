# Clase 17 Funciones de Cadenas 1a Parte

# En esta clase veremos un tema fundamental para lo que es el manejo de las cadenas; y son sus
# funciones.

# Debido a que son muchas funciones, hemos seleccionado las mas importantes y fundamentales y esta
# clase estará divida en 2 partes

# No se expone la tabla con la información de cada una de ellas sino, que al momento de mostrar el
# ejemplo se explicará su forma de uso.


# Desplegamos Mensaje de la Clase
print("Clase 17 Funciones de Cadenas 1a Parte")
print()

#Declaramos una variable de Cadena
#           123456789-123456789-123456789-123456789-123456
sMensaje = "este es un Mensaje utilizado como Prueba. Fin."

print("capitalize:",sMensaje.capitalize())
print("center:",sMensaje.center(80,"-"))
print()

print("count:",sMensaje.count("es"))
print("count:",sMensaje.count("a",4))
print("count:",sMensaje.count("4",4,20))
print()

print("endswith:",sMensaje.endswith("Fin."))
print("endswith:",sMensaje.endswith("Fin.",4))
print("endswith:",sMensaje.endswith("Mensaj",0,17))
print()

print("find:",sMensaje.find("un"))
print("find:",sMensaje.find("un",5))
print("find:",sMensaje.find("un",10,20))
print()

print("index:",sMensaje.index("un"))
print("index:",sMensaje.index("un",5))
print("index:",sMensaje.index("un",5,20))
print()

print("isalpha:",sMensaje.isalpha())
sMensaje="Minumerotelefonico12112312312"
print("isalpha:",sMensaje.isalpha())
sMensaje="Minumerotelefonico"
print("isalpha:",sMensaje.isalpha())
print()

sMensaje="este es un Mensaje utilizado como Prueba. Fin."
print("isalnum:",sMensaje.isalnum())
sMensaje="Mi numero telefonico es 12112312312"
print("isalnum:",sMensaje.isalnum())
sMensaje="Minumerotelefonicoes12312312312"
print("isalnum:",sMensaje.isalnum())
print()

sMensaje="este es un Mensaje utilizado como Prueba. Fin."
print("isdigit:",sMensaje.isdigit())
print("isnumeric:",sMensaje.isnumeric())
sMensaje="123 123 1234"
print("isdigit:",sMensaje.isdigit())
print("isnumeric:",sMensaje.isnumeric())
sMensaje="1231231234"
print("isdigit:",sMensaje.isdigit())
print("isnumeric:",sMensaje.isnumeric())
print()

sMensaje="este es un Mensaje utilizado como Prueba. Fin."
print("islower:",sMensaje.islower())
sMensaje="este es un mensaje utilizado como prueba. fin."
print("islower:",sMensaje.islower())
print()

sMensaje="este es un Mensaje utilizado como Prueba. Fin."
print("isspace:",sMensaje.isspace())
sMensaje="      "
print("isspace:",sMensaje.isspace())
print()

sMensaje="este es un Mensaje utilizado como Prueba. Fin."
print("istitle:",sMensaje.istitle())
sMensaje="Este Es Un Mensaje Utilizado Como Prueba. Fin."
print("istitle:",sMensaje.istitle())
print()

sMensaje="este es un Mensaje utilizado como Prueba. Fin."
print("isupper:",sMensaje.isupper())
sMensaje="ESTE ES UN MENSAJE UTILIZADO COMO PRUEBA. FIN."
print("isupper:",sMensaje.isupper())
print()

# Variable con datos a unir
sep="|"
nombres =("Juan","Pedro","Alberto")
print("join",sep.join(nombres))
print("join","-".join(nombres))
print("join","<->".join(nombres))
print()

print("len:",len(sMensaje))
print()

print("ljust:",sMensaje.ljust(70,"0"))
print("ljust:",sMensaje.ljust(50,"*"))


