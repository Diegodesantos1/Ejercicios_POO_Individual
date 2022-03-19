"""Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido,
se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes? """
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
        print("\nExplicación: se printeaba antes ? ya que del(yang) no era accesible,\nya que es un atributo privado devido a las (__) __del__\nal nombrarlo correctamente ahora sí, se ejecuta antes\n")