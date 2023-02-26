# Función recursiva para imprimir los números de 1 hasta n

def imprimir_numerosde1HastaN(n):
    if n == 1:
        return print(n)
    else:
        return imprimir_numerosde1HastaN(n-1), print(n)


imprimir_numerosde1HastaN(3)
