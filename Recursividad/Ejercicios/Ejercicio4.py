# Función recursiva para imprimir los números de 1 hasta n

def ImprimirNumerosDe1Hastan(n):
    if n == 1:
        return 1
    else:
        return print(ImprimirNumerosDe1Hastan(n - 1))


print(ImprimirNumerosDe1Hastan(3))
