# Dada una lista l, diga si un elemento e está en la lista o no. (Recursivo)

def VerficarExistenciaDeElementoEnUnaLista(lista,numero):
    if len(lista) == 0:
        return print("No esta")
    if numero == lista[0]:
        print("Esta")
    else:
        VerficarExistenciaDeElementoEnUnaLista(lista[1:], numero)


lista = [1,2,3,4,5,6]
numero = 7
VerficarExistenciaDeElementoEnUnaLista(lista,numero)