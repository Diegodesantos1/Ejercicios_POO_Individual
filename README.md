<h1 align="center">Ejercicios Individuales POO</h1>

*He usado la Programación Orientada a Objetos para resolver estos ejercicios.*

---

En este [repositorio](https://github.com/Diegodesantos1/Ejercicios_POO_Individual) quedan resueltos los ejercicios de POO en Python. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y de otros medios.

***
## Índice
1. [Ejercicio 1: Catástrofe ](#id1)
2. [Ejercicio 2: Inmortal](#id2)
3. [Ejercicio 3: Alternativa a la Herencia múltiple](#id3)

***

## Ejercicio 1: Catástrofe <a name="id1"></a>

Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.


```python
from colorama import Fore
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
            print(Fore.LIGHTRED_EX + "¡Oh no, está cayendo un meteorito en Nueva York!\n" + Fore.WHITE)
            final1 = A.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final2 = B.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final3 = C.ocurrir_catastrofe()
            print(f" {final1}\n {final2}\n {final3}\n")
        elif eleccion == 2:
            print(Fore.LIGHTRED_EX +"¡Oh no, está cayendo un meteorito en Los Ángeles!\n" + Fore.WHITE)
            final1 = A.ocurrir_catastrofe() ; final2 = B.ocurrir_catastrofe() ; final3 = C.ocurrir_catastrofe().replace ("Los Ángeles","Destruida")
            print (f" {final1}\n {final2}\n {final3}\n")
        elif eleccion == 3:
            print(Fore.LIGHTRED_EX +"¡Oh no, está cayendo un meteorito en Los Ángeles y en Nueva Yotk!\n"+ Fore.WHITE)
            final1 = A.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final2 = B.ocurrir_catastrofe().replace ("Nueva York","Destruida") ; final3 = C.ocurrir_catastrofe().replace ("Los Ángeles","Destruida")
            print (f" {final1}\n {final2}\n {final3}\n")
        else:
            Dia_siguiente.activar()
```

Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159304406-c755e7a3-4c03-4ee1-b611-6ec88cdff7b0.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Individual/blob/main/UML/Catastrofe.drawio)


## Ejercicio 2: ¿Inmortal? <a name="id2"></a>

Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?

```python
class Inmortal:
    def ejecutar_ejercicio():
        class Yin: pass
        class Yang:
            def _del_(self):
                print("Yang destruido")

        yin = Yin()
        yang = Yang()
        yin.yang = yang

        print(yang)
        print(yang is yin.yang)
        Yang._del_(yang)
        print("?")
        print("\nExplicación: se printeaba antes ? ya que del(yang) no era accesible,\nya que es un atributo privado debido a las (__) __del__\nal nombrarlo correctamente ahora sí, se ejecuta antes\n")
```

Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159304695-8cddf74a-58c3-4c78-91f7-5bca97f3f4bc.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Individual/blob/main/UML/Inmortal.drawio)

## Ejercicio 3: Alternativa a la Herencia múltiple <a name="id3"></a>

Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.

Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.

Enunciado: modifique el código para que el programa funcione de nuevo.

Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159433629-6f070b4e-6240-45c2-92c7-a48e85a1b6ef.png)

En formato [XML](https://github.com/Diegodesantos1/Ejercicios_POO_Individual/blob/main/UML/Herencia_Ejercicio3.drawio)

```python
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

Interfaz_Cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
print("\n")
Interfaz_Cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
print("\n")
Interfaz_Cristal().ParedCortina('NORTE', 4)
print("\n")
Interfaz_Cristal().Superficie()
print("\n")
Interfaz_Cristal().ComprobarProteccion('NORTE')
```
