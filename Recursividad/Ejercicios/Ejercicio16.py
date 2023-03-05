# Escriba una función recursiva para
# determinar si un número n es primo o no

"""def esPrimoONo(numero,contador = 0, divisor =1):
    if numero % divisor == 0:
        contador += 1
        esPrimoONo(numero,contador,divisor+1)
    if contador == 2:
        return print("Es primo")
    if contador > 2:
        return print("No es primo")


esPrimoONo(7)"""



def cantidadDeDivisores(numero,contador=0,divisor=1):
    if numero == divisor:
        return contador
    if numero % divisor == 0:
        contador +=1
    else:
        cantidadDeDivisores(numero,contador,divisor+1)


cantidadDeDivisores(7)

