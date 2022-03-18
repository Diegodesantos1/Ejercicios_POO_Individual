
class Catastrofe:
    def __init__(self,ciudad,empresa,empleado):
        self.ciudad=ciudad
        self.empresa=empresa
        self.empleado=empleado
    def ocurrir_catastrofe(self):
        txt= "{0} {1} {2}"
        return txt.format(self.ciudad, self.empresa,self.empleado)
A=Catastrofe("Nueva York","YooHoo!","Martin")
B=Catastrofe("Nueva York","YooHoo!","Salim")
C=Catastrofe("Los Ángeles","YooHoo!","Xing")