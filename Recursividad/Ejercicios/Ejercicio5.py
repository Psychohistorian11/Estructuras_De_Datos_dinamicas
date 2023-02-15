# Imprimir todos los elementos de una lista

def ImprimirTodosLosElementos(lista):
    if len(lista) != 0:
        print(lista[0])
        ImprimirTodosLosElementos(lista[1:])


lista = [1, 2, 3, 4, 5]

print(ImprimirTodosLosElementos(lista))
