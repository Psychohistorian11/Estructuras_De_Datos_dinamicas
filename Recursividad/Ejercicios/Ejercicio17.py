def es_primo(n, i=2):
    """
    Determina si un número n es primo o no de forma recursiva.
    """
    if n <= 1:  # Caso base: 1 o números negativos no son primos
        return False
    elif i == n:  # Caso base: n es primo si i es igual a n
        return True
    elif n % i == 0:  # Caso base: n no es primo si es divisible por i
        return False
    else:
        # Llamada recursiva: incrementa i y llama la función nuevamente
        return es_primo(n, i + 1)


print(es_primo(8))