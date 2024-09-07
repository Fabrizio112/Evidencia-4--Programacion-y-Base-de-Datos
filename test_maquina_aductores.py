from maquina_aductores import *

def test_maquina_ctr():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.get_peso()== 0
    assert maquina.get_posicion() == "ADUCTORES"

def test_maquina_str():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.__str__() == "La maquina de aductores posee 0 kg y se encuentra en posicion para trabajar el grupo muscular ADUCTORES"

def test_maquina_get_peso():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.get_peso() == 0

def test_maquina_get_posicion():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.get_posicion() == "ADUCTORES"

def test_maquina_set_peso():
    maquina=MaquinaAductores(0,"Aductores")
    maquina.set_peso(10)
    assert maquina.get_peso() == 10

def test_maquina_set_posicion():
    maquina=MaquinaAductores(0,"Aductores")
    maquina.set_posicion("abductores")
    assert maquina.get_posicion() == "ABDUCTORES"

def test_maquina_cambiar_misma_posicion():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.cambiar_posicion("Aductores") == "Ya la máquina se encuentra en esta posicion" and maquina.get_posicion() == "ADUCTORES"

def test_maquina_cambiar_posicion():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.cambiar_posicion("Abductores") == "Se cambia la posicion de la máquina a ABDUCTORES" and maquina.get_posicion()== "ABDUCTORES"

def test_maquina_aumentar_peso():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.aumentar_peso() == (maquina.get_peso() == 5 and "Aumentando el peso de la máquina") 

def test_maquina_aumentar_peso_maximo():
    maquina=MaquinaAductores(100,"Aductores")
    assert maquina.aumentar_peso() == (maquina.get_peso() == 100 and "No se puede aumentar mas el peso de la máquina")

def test_maquina_disminuir_peso():
    maquina=MaquinaAductores(5,"Aductores")
    assert maquina.disminuir_peso() == (maquina.get_peso() == 0  and "Disminuyendo el peso de la máquina")
def test_maquina_disminuir_minimo_peso():
    maquina=MaquinaAductores(0,"Aductores")
    assert maquina.disminuir_peso() == (maquina.get_peso() == 0  and "No se puede disminuir el peso de la máquina")