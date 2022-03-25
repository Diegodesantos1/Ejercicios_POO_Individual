class Catastrofe:
    def __init__(self,ciudad,empresa,empleado):
        self.ciudad=ciudad ; self.empresa=empresa ; self.empleado=empleado
    def ocurrir_catastrofe(self):
        txt= "{0},{1},{2}"
        return txt.format(self.ciudad, self.empresa,self.empleado)
class Dia_siguiente(Catastrofe):
    def activar():
        A=Catastrofe("Nueva York","YooHoo!","Martin") ; B=Catastrofe("Nueva York","YooHoo!","Salim") ; C=Catastrofe("Los Ángeles","YooHoo!","Xing")
        print(A.ocurrir_catastrofe()) ; print(B.ocurrir_catastrofe()) ; print(C.ocurrir_catastrofe())
        eleccion=int(input("\n¿Qué ciudad desea destruir?\n --> 1: Nueva York\n --> 2: Los Ángeles\n -- >3: Ambas\n"))
        if eleccion == 1:
            print("¡Oh no, está cayendo un meteorito en Nueva York!\n")
            final1 = A.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final2 = B.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final3 = C.ocurrir_catastrofe()
            print(f" {final1}\n {final2}\n {final3}\n")
        elif eleccion == 2:
            print("¡Oh no, está cayendo un meteorito en Los Ángeles!\n")
            final1 = A.ocurrir_catastrofe() ; final2 = B.ocurrir_catastrofe() ; final3 = C.ocurrir_catastrofe().replace ("Los Ángeles","Destruida")
            print (f" {final1}\n {final2}\n {final3}\n")
        elif eleccion == 3:
            print("¡Oh no, está cayendo un meteorito en Los Ángeles y en Nueva Yotk!\n")
            final1 = A.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final2 = B.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final3 = C.ocurrir_catastrofe().replace ("Los Ángeles","Destruida")
            print (f" {final1}\n {final2}\n {final3}\n")
        else:
            eleccion=int(input("\n¿Qué ciudad desea destruir?\n --> 1: Nueva York\n --> 2: Los Ángeles\n -- >3: Ambas"))

