#Este código pide un número n y un número r, luego entrega todos los subconjuntos de Zn tales que, sean conjuntos profundos de Erdos de tamaño r; finalmente los cuenta
from itertools import combinations
from collections import Counter

def construir_y_encontrar_subconjuntos(n, r):
    Z = set(range(n))
    subconjuntos = list(combinations(Z, r))
    return subconjuntos

def calcular_distancias(subconjunto, n):
    distancias = []
    for i, x in enumerate(subconjunto):
        for y in subconjunto[i+1:]:
            distancia = min(abs(x - y), n - abs(x - y))
            distancias.append(distancia)
    multiconjunto_distancias = Counter(distancias)
    return multiconjunto_distancias

def listar_subconjuntos_unicos(subconjuntos, n):
    count = 0
    for subconjunto in subconjuntos:
        distancias_subconjunto = calcular_distancias(subconjunto, n)
        
        # Verificar si las ocurrencias de las distancias son únicas y conforman el conjunto {1, 2, ..., len(subconjunto)-1}
        if set(distancias_subconjunto.values()) == set(range(1, len(subconjunto))):
            print(f"Subconjunto: {subconjunto}, Multiconjunto de distancias: {distancias_subconjunto}")
            count += 1

    return count

# Ejemplo de uso
n = int(input("Ingrese un número n: "))
r = int(input("Ingrese el tamaño del subconjunto r: "))
subconjuntos = construir_y_encontrar_subconjuntos(n, r)

print(f"Subconjuntos con ocurrencias de distancias únicas y conforman el conjunto {{1, 2, ..., len(subconjunto)-1}} de tamaño {r}:")
cantidad_subconjuntos = listar_subconjuntos_unicos(subconjuntos, n)
print(f"La cantidad de subconjuntos que cumplen con las condiciones adicionales es: {cantidad_subconjuntos}")


