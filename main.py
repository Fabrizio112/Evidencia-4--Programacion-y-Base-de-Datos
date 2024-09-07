from maquina_aductores import *

if __name__ == "__main__":
    maquina = MaquinaAductores(30,"ADUCTORES")
    print(maquina.__str__())
    print(maquina.get_peso())
    print(maquina.get_posicion())
    maquina.cambiar_posicion("ABDUCTORES")
    print(maquina.__str__())
    maquina.aumentar_peso()
    print(maquina.__str__())
    maquina.disminuir_peso()
    print(maquina.__str__())
    maquina.disminuir_peso()
    print(maquina.__str__())
    #OTRA OBJETO MAQUINA
    print("")
    maquina_peso_minimo=MaquinaAductores(0,"ABDUCTORES")
    print(maquina_peso_minimo.__str__())
    print(maquina_peso_minimo.disminuir_peso())
     #OTRA OBJETO MAQUINA
    print("")
    maquina_peso_maximo=MaquinaAductores(100,"ABDUCTORES")
    print(maquina_peso_maximo.__str__())
    print(maquina_peso_maximo.aumentar_peso())
    