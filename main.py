from maquina_aductores import *

if __name__ == "__main__":
    maquina = MaquinaAductores(30,"ADUCTORES")
    print(maquina.__str__())
    maquina.cambiar_posicion("ABDUCTORES")
    print(maquina.__str__())