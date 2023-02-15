"""Crea una función que calcule el valor de elevar un
número entero a otro número entero (por ejemplo, 4
elevado a 3 = 4 * 4 * 4 = 64). Esta función se debe
crear de forma recursiva. Piensa cuál será el caso
base (qué potencia se puede calcular de forma trivial)
y cómo pasar del caso "n-1" al caso "n" (por ejemplo,
si sabes el valor de 54, cómo hallarías el de 55 a partir de él)."""


def Potencia(numero1, numero2):
    if numero2 == 0:
        return 1
    else:
        return numero1 * Potencia(numero1, numero2 - 1)


print(Potencia(2, 3))
