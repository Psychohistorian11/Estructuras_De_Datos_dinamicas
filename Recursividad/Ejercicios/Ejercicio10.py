# Defina una función recursiva que reciba una
# lista para determinar cuántos numeros pares hay en ella

def cuantosNumerosParesHay(lista, c=0):
    if len(lista) != 0:
        if (lista[0] % 2) == 0:
            c += 1
            cuantosNumerosParesHay(lista[1:], c)
        else:
            cuantosNumerosParesHay(lista[1:], c)
    else:
        return print(c)


l = [1, 3, 5, 7]

cuantosNumerosParesHay(l)

