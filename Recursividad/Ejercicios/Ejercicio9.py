# Defina una función recursiva para determinar la
# cantidad de elementos en una lista l

def CantidadDeElementosEnUnaLista(l,c):
    if len(l) != 0:
        c += 1
        CantidadDeElementosEnUnaLista(l[1:],c)
    else:
        return print(c)


c = 0
lista = [1,2,3]
CantidadDeElementosEnUnaLista(lista,c)
