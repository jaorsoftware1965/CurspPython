# Clase 88

# Como usar una Función Api de Windows desde Python

# Importamos ctypes
import ctypes

# Cargamos la Función DLL que queremos usar
dialogo_windows = ctypes.windll.user32.MessageBoxW

# Ejecutamos
dialogo_windows(None,"HOLA MUNDO!","Win API",0x40 | 0x0)

