from Clases.Catastrofe import Dia_siguiente
from Clases.Inmortal import Inmortal
from Clases.alternativa import *

def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Catástrofe\n -->2: Inmortal \n -->3: Alternativa \n"))
    if variable == 1:
        Dia_siguiente.activar()
    elif variable == 2:
        Inmortal.ejecutar_ejercicio()
    elif variable == 3:
        Interfaz_Cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
        print("\n")
        Interfaz_Cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
        print("\n")
        Interfaz_Cristal().ParedCortina('NORTE', 4)
        print("\n")
        Interfaz_Cristal().Superficie()
        print("\n")
        Interfaz_Cristal().ComprobarProteccion('NORTE')
    else:
        eleccion_ejercicio()

eleccion_ejercicio()