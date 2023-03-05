# Ejercicio numero 8
# Given a string find its first uppercase letter
def primeraMayuscula(string, i=0):
    string1 = is_mayus(string[0])
    if string1:
        return string[0]
    else:
        return primeraMayuscula(string[i + 1], i + 1)


def is_mayus(letra):
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                  "U", "V", "W", "Y", "Z"]
    for i in letra:
        if i in mayusculas:
            return True
        else:
            return False


print(primeraMayuscula("aHla"))
