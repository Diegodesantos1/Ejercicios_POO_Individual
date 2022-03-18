class Catastrofe:
    def __init__(self,ciudad,empresa,empleado):
        self.ciudad=ciudad
        self.empresa=empresa
        self.empleado=empleado
    def ocurrir_catastrofe(self):
        txt= "{0},{1},{2}"
        return txt.format(self.ciudad, self.empresa,self.empleado)
class Catastrofe_activada(Catastrofe):
    A=Catastrofe("Nueva York","YooHoo!","Martin")
    B=Catastrofe("Nueva York","YooHoo!","Salim")
    C=Catastrofe("Los Ángeles","YooHoo!","Xing\n")
    print(A.ocurrir_catastrofe())
    print(B.ocurrir_catastrofe())
    print(C.ocurrir_catastrofe())
    print("¡Oh no, está cayendo un meteorito el Nueva York!\n")
    print(A.ocurrir_catastrofe().replace ("Nueva York","Destruida"))
    print(B.ocurrir_catastrofe().replace ("Nueva York","Destruida"))
    print(C.ocurrir_catastrofe())
