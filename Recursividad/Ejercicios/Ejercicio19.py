# Escriba una función recursiva que reciba una lista
# de palabras y retorne una lista con las palabras que
# contengan mayúsculas y otra lista con las que no tienen.
def tieneMayuscula(palabra):
    if len(palabra) == 0:
        return False
    if palabra[0].isupper():
        return True
    else:
        return tieneMayuscula(palabra[1:])


def mayusculasYMinusculas(listaDePalabras, Mayusculas=None, minusculas=None):
    if minusculas is None:
        minusculas = []
    if Mayusculas is None:
        Mayusculas = []
    if len(listaDePalabras) == 0:
        return Mayusculas,minusculas
    if tieneMayuscula(listaDePalabras[0]):
        Mayusculas.append(listaDePalabras[0])
    if not tieneMayuscula(listaDePalabras[0]):
        minusculas.append(listaDePalabras[0])

    return mayusculasYMinusculas(listaDePalabras[1:],Mayusculas,minusculas)


listaDePalabras = ["Este Algoritmo", "es capaz de", "Clasificar", "las palabras que",
                   "Tengan Mayusculas", "y", "minusculas","En dos listas diferentes", "es increible"]
lista1, lista2 = mayusculasYMinusculas(listaDePalabras)
print(lista1)
print(lista2)


