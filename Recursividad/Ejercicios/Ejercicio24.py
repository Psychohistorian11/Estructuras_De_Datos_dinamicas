def MaxyMin(array):
    return Max(array),Min(array)



def Max(array, bandera=0):
    if len(array) == 0:
        return bandera
    if array[0] > bandera:
        bandera = array[0]
        return Max(array[1:], bandera)
    return Max(array[1:], bandera)

def Min(array, bandera=0):
    if len(array) == 0:
        return bandera
    if array[0] < bandera:
        bandera = array[0]
        return Max(array[1:], bandera)
    return Max(array[1:], bandera)


array = [1, 4, 6, 9, 3, 6, 16, 5, 4]
a,b = MaxyMin(array)
print(a,b)

