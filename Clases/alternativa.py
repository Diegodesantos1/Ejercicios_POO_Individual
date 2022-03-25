casa = {}
orientaciones = ['NORTE', 'SUR', 'ESTE', 'OESTE']

class Interfaz_Cristal():
    global casa
    def Paredes(self, orientacion):
        for i in range(len(orientacion)):
            nombre = orientacion[i]
            casa[nombre] = {'ventanas': {},}
        print(casa)
        Interfaz_Cristal().Ventanas([['NORTE', 0.5, ''], ['SUR', 1, ''], ['ESTE', 2, ''], ['OESTE', 1, '']])
    def Ventanas(self, ventanas):
        dimensiones = []
        for i in range(len(ventanas)):
            nombre = ventanas[i][0]
            casa[nombre]['ventanas'] = {'superficie': ventanas[i][1],'proteccion': ventanas[i][2]}
        dimensiones.append(ventanas[i][1])
        print(casa)
        Interfaz_Cristal().Superficie()
    def Superficie(self):
        total = 0
        for i in range(len(orientaciones)):
            total += casa[orientaciones[i]]['ventanas']['superficie']
        print('Superficie acristalada: ' + str(total))
    def ParedCortina(self, orientacion, tamaño):
        casa[orientacion]['ventanas']['superficie'] += tamaño
        print(casa)
    def ComprobarProteccion(self, orientacion):
        if casa[orientacion]['ventanas']['proteccion'] != '':
            print('Protección en regla.')
        else:
            print('Protección obligatoria no presente.')