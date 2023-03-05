# Escriba una función recursiva que imprima
# los números desde un número n hasta otro número m descendentemente

def ImprimirNumerosDeNHastaM(n,m):
    if m != n:
        print(m)
        ImprimirNumerosDeNHastaM(n, m-1)
    else:
        print(n)


ImprimirNumerosDeNHastaM(3,8)
