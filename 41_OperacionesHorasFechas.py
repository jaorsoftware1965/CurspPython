# Clase 41 Operaciones con Horas y Fechas

print("Clase 41 Operaciones con Horas y Fechas")
print()

# En esta clase veremos como realizar operaciones con Horas y Fechas
# utilizando los módulos vistos previamente


# Importamos las librerías
from datetime import datetime, date, time, timedelta

# Mensaje
print("Comparando Horas")
print()

# Crea 2 horas y las despliega
hora1 = time(10, 5, 0)  
print("Hora1:", hora1)

hora2 = time(23, 15, 0)
print("Hora2:", hora2)

# Comparamos las Horas
print("Hora1 < Hora2:", hora1 < hora2)
print()

print("Comparando Fechas")
print()

# Creando 2 fechas
fecha1 = date.today()  # Asigna fecha actual
print("Fecha1:", fecha1)

# Suma a la fecha actual 2 días
fecha2 = date.today() + timedelta(days=2)
print("Fecha2:", fecha2)

# Compara fechas
print("Fecha1 > Fecha2:", fecha1 > fecha2)
print()

# Obteniendo Fechas Anteriores y posteriores
print("Fechas Anteriores y Posteriores")

# Obtenemos la Fecha de Hoy y la desplegamos
hoy = datetime.now() 
#hoy = datetime.today()
print("Hoy   :",hoy,"Tipo:",type(hoy))

# Calculamos la Fecha de ayer
ayer = hoy + timedelta(days=-1) # Ojo sobre el Operador -
print("Ayer  :",ayer,"Tipo:",type(ayer))

# Calculamos la fecha de mañana
maniana = hoy + timedelta(days=1)
print("Mañana:",maniana,"Tipo",type(maniana))

# Calculamos la diferencia en días
diferencia_en_dias = maniana - ayer  # Resta las dos fechas
print("Diferencia:",diferencia_en_dias)
print()

# Diferencia en Horas desde now
print("Fechas con Horas Anteriores y Posteriores")

# Calculando horas despues de hoy
hoy5HrsDespues = hoy + timedelta(hours=5)
print("Hoy 5 hrs despues:",hoy5HrsDespues,"Tipo",type(hoy5HrsDespues))

# Calculando horas antes de hoy
hoy5HrsAntes = hoy + timedelta(hours=-5)
print("Hoy 5 hrs antes:",hoy5HrsAntes,"Tipo",type(hoy5HrsAntes))

# Calculando minutos despues de hoy
hoy5MinsDespues = hoy + timedelta(minutes=5)
print("Hoy 5 Mins despues:",hoy5MinsDespues,"Tipo",type(hoy5HrsDespues))

# Calculando minutos antes de hoy
hoy5MinsAntes = hoy + timedelta(minutes=-5)
print("Hoy 5 Mins antes:",hoy5MinsAntes,"Tipo",type(hoy5HrsAntes))
