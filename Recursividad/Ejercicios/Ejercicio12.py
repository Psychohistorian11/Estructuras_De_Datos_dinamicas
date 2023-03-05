# Escriba una función recursiva que reciba un
# número y retorne la cantidad de dígitos de este número.

def CantidadDeDigitos(numero,c=1):
    if numero // 10 != 0:
        c += 1
        CantidadDeDigitos(numero//10,c)
    else:
        print(c)


CantidadDeDigitos(24654634)