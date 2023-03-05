# Escriba una función recursiva que invierta un string dado

"""def invertirString(string, stringInvertido=""):
    if len(string) == 0:
        return stringInvertido
    else:
        stringInvertido += string[-1]
        invertirString(string[1:])
    return print(stringInvertido)


invertirString("hola")"""

def invertirString(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + invertirString(string[:-1])


print(invertirString("En este momento y a través de estas simples "
                     "palabras se revelara como soy capaz de invocar "
                     "a lucifer"))
