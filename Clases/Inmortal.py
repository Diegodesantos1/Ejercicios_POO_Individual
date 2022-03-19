"""Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido,
se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes? """

class Yin: pass
class Yang:
    def __del__(self):
        print("Yang destruido")

yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)
print(yang is yin.yang)
del(yang)
print("?")