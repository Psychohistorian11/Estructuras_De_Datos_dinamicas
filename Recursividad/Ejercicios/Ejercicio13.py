# Escriba una función recursiva que encuentre
# el mínimo común múltiplo de dos números n y m.

def minimoComunMultiplo(n,m,factoresprimos=2,multiplo=1):
    if (n // factoresprimos == 0) or (m // factoresprimos == 0):
        return factoresprimos
    else:
        return multiplo * minimoComunMultiplo(n,m,factoresprimos+1)

