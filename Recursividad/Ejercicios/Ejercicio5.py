# Imprimir todos los elementos de una lista

"""def ImprimirTodosLosElementos(lista):
    if len(lista) != 0:
        print(lista[0])
        ImprimirTodosLosElementos(lista[1:])"""


lista = [1, 2, 3, 4, 5]

#ImprimirTodosLosElementos(lista)


def ImprimirTodosLosElementos2(lista):
    if len(lista) == 0:
        return 0
    else:
        return print(lista[0]),ImprimirTodosLosElementos2(lista[1:])


ImprimirTodosLosElementos2(lista)