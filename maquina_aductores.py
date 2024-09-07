class MaquinaAductores():
  def __init__(self, peso ,posicion):
    self.__peso=peso
    self.__posicion=posicion.upper()

  def __str__(self):
    return f"La maquina de aductores posee {self.__peso} kg y se encuentra en posicion para trabajar el grupo muscular {self.__posicion}"
  
  def get_peso(self):
    return self.__peso
  
  def set_peso(self,peso):
    self.__peso=peso

  def get_posicion(self):
    return self.__posicion
  
  def set_posicion(self,posicion):
    self.__posicion=posicion.upper()

  def cambiar_posicion(self,nueva_posicion):
    if (self.get_posicion() == nueva_posicion.upper()):
      return "Ya la máquina se encuentra en esta posicion"
    else:
      self.set_posicion(nueva_posicion)
      return "Se cambia la posicion de la máquina a ABDUCTORES"
  def aumentar_peso(self):
    peso_maximo=100
    if(self.get_peso() == peso_maximo):
      return "No se puede aumentar mas el peso de la máquina"
    else:
      self.set_peso(+5)
      return "Aumentando el peso de la máquina"
  def disminuir_peso(self):
    peso_minimo=0
    if (self.get_peso() == peso_minimo):
      return "No se puede disminuir el peso de la máquina"
    else:
        self.set_peso(self.__peso - 5)
        return "Disminuyendo el peso de la máquina"