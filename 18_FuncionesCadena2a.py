# Clase 18 Funciones de Cadenas 2a Parte

# En esta clase continuaremos viendo las Funciones de Cadena

# Desplegamos Mensaje de la Clase
print("Clase 18 Funciones de Cadenas 2a Parte")
print()

#Declaramos una variable de Cadena
#           123456789-123456789-123456789-123456789-123456
sMensaje = "este es un Mensaje utilizado como Prueba. Fin."

print("lower:",sMensaje.lower())
print()

sMensaje = "     este es un Mensaje utilizado como Prueba. Fin."
print("lstrip:",sMensaje.lstrip())
sMensaje = "88888888este es un Mensaje utilizado como Prueba. Fin.8888888"
print("lstrip:",sMensaje.lstrip('8'))
print()

# Cadena origen y cadena destino
intab  = "aeiou"
outtab = "12345"

codificacion = sMensaje.maketrans(intab,outtab)
sMensaje = "este es un Mensaje utilizado como Prueba. Fin."
print("translate:",sMensaje.translate(codificacion))

print("max:",max(sMensaje))
print("min:",min(sMensaje))
print("min:",min("mensaje"))

print("replace:",sMensaje.replace("e","eje"))
print("replace:",sMensaje.replace("e","eje",2))
print()

print("rfind:",sMensaje.rfind("es"))
print("rfind:",sMensaje.rfind("es",0,30))
print("rfind:",sMensaje.rfind("es",10,45))
print()

print("rindex:",sMensaje.rindex("es"))
print("index:",sMensaje.index("es"))
print()

sMensaje="    Este es un Mensaje con espacios antes y despues   "
print("Longitud:",len(sMensaje))
sMensaje = sMensaje.rstrip()
print("Longitud:",len(sMensaje))
print("rstrip",sMensaje)
sMensaje="******* Este es un Mensaje con asteriscos antes y despues *****"
print("rstrip",sMensaje.rstrip("*"))
print()

sMensaje = "este es un Mensaje utilizado como Prueba. Fin."
print("split:",sMensaje.split())
print("split:",sMensaje.split(' ',2))
print("split:",sMensaje.split('e'))
print()

sMensaje = "Linea 1 - a b c d e f\nLinea 2- a b c\n\nLinea 4 - a b c d";
print("splitlines:",sMensaje.splitlines())
print("splitlines:",sMensaje.splitlines(False))
print("splitlines:",sMensaje.splitlines(True))
print("splitlines:",sMensaje.splitlines(4))

sMensaje = "este es un Mensaje utilizado como Prueba. Fin."
print("startswith:",sMensaje.startswith("este"))
print("startswith:",sMensaje.startswith("este",5))
print("startswith:",sMensaje.startswith("un",8,20))
print()

sMensaje = "******este es un Mensaje utilizado como Prueba. Fin. *****"
print("strip:",sMensaje.strip("*"))
print()

sMensaje = "este es un Mensaje utilizado como Prueba. Fin."
print("swapcase:",sMensaje.swapcase())
print()

print("title:",sMensaje.title())
print()

print("upper:",sMensaje.upper())
print()

print("zfill:",sMensaje.zfill(50))
print()

print("isdecimal:",sMensaje.isdecimal())
sMensaje="12312312349870"
print("isdecimal:",sMensaje.isdecimal())

