# Sumar cada componente de un numero

def sumarComponentesDeUnNumero(numero):
    if (numero % 10) == 0:
        return 0
    else:
        return numero % 10 + sumarComponentesDeUnNumero(numero // 10)


print(sumarComponentesDeUnNumero(345))
