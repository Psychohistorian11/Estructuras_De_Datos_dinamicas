# Given an array of integers, print a sum triangle from it such that the first level
# has all array elements. From then, at each level number of elements is one less than
# the previous level and elements at the level is be the Sum of consecutive two elements
# in the previous level.


def triangulodelArray(array):
    if len(array) == 1:
        print(array)
    else:
        print(array)
        siguienteArray = sumarComponentesDeArray(array)
        return triangulodelArray(siguienteArray)


def sumarComponentesDeArray(array, siguienteArray=None):
    if siguienteArray is None:
        siguienteArray = []
    if len(array) == 1:
        return array
    else:
        siguienteArray.append(array[0] + array[1])
        sumarComponentesDeArray(array[1:], siguienteArray)
        return siguienteArray


a = [1, 4, 6, 8, 5, 3, 2]
triangulodelArray(a)
