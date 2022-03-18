from Clases import Catastrofe
from Clases.Catastrofe import *


def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Catástrofe\n -->2: \n -->3: \n -->4: \n"))
    if variable == 1:
        Catastrofe.ocurrir_catastrofe()
    elif variable == 2:
        from Clases import ejercicio2
    elif variable == 3:
        from Clases import ejercicio3
    elif variable == 4:
        from Clases import ejercicio3
    else:
        eleccion_ejercicio()

eleccion_ejercicio()