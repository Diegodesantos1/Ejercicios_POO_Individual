from Clases.Catastrofe import Dia_siguiente
from Clases.Inmortal import Inmortal


def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Catástrofe\n -->2: Inmortal \n -->3: \n -->4: \n"))
    if variable == 1:
        Dia_siguiente.activar()
    elif variable == 2:
        Inmortal.ejecutar_ejercicio()
    elif variable == 3:
        from Clases import ejercicio3
    else:
        eleccion_ejercicio()

eleccion_ejercicio()