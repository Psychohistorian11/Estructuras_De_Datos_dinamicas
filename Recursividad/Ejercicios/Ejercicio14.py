#  Escriba una función recursiva que
#  encuentre el mínimo de una lista l dada

def valorMinimo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > lista[1]:
        return valorMinimo(lista[1:])
    else:
        return lista[0]


lista = [10, 9, 2, 4,1,3]
a = valorMinimo(lista)
print(a)

