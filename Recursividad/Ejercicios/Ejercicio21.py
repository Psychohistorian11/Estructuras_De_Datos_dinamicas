""" Cree una función recursiva de cola que reciba
un entero y retorne cuántos dígitos de este número son múltiplos de 3 o de 5.

Por ejemplo: si la función recibe el número 34523,
 deberá retornar 3 ya que hay tres números que son
 múltiplos de 3 o de 5 (el primer 3, el 5 y el último 3)."""


def MultiplosDe3oDe5(entero):
    if entero % 10 == 0:
        return 0
    if (entero%10)%3 == 0 or (entero%10)%5 == 0:
        return 1 + MultiplosDe3oDe5(entero//10)
    else:
        return MultiplosDe3oDe5(entero//10)


print(MultiplosDe3oDe5(3495))

