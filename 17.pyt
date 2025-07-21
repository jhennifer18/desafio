import random

def simular_dado(n):
    resultados = []
    for _ in range(n):
        resultados.append(random.randint(1, 6))
    return resultados
