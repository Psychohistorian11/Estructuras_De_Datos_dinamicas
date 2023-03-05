# Escriba una función recursiva que reciba un srtring alfanumérico
# y retorne el máximo de los dígitos en el string. Por ejemplo:
# en el string "hola123" debe retornar 3 ya que el máximo digito es 3

def maximoDigitoDelStringAlfanomerico(string, numeroMayor=None):
    if numeroMayor is None:
        numeroMayor = 0
    if len(string) == 0:
        return numeroMayor
    elif string[0] is int:
        pass

