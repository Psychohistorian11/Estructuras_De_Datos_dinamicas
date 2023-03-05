"""Cree una función no recursiva de cola que
invierta sólo la primera mitad de un string.

Por ejemplo, si la función recibe "Hola", deberá retornar "oHla".
Asuma que el punto medio es tamaño//2"""


def invertirAlaMitad(string):
    mitad = string//2
    if len(string) == 0:
        return 0
    if string[0] < mitad:
        return print(string)
