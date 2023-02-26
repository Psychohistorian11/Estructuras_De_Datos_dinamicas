"""Realizar una calculadora que pase
 de entero(Positivos y negativos) a binario"""

numero = int(input("Ingrese numero: "))


def pasarABinario(numero, bin=""):
    if numero < 2:
        numero = str(numero)
        bin += numero
        return bin[::-1]
    else:
        dig = str(numero % 2)
        bin += dig
        numero = numero // 2
        return pasarABinario(numero,bin)


print(pasarABinario(45))
