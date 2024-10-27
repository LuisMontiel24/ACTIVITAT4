import random

def crear_matriu_aleatoria(files, columnes):
    return [[random.randint(0, 100) for _ in range(columnes)] for _ in range(files)]

def redimensionar_matriu(matriu, files, columnes):
    elements = [element for fila in matriu for element in fila]
    if len(elements) != files * columnes:
        raise ValueError("Les noves dimensions no coincideixen amb el nombre d'elements")
    return [elements[i * columnes:(i + 1) * columnes] for i in range(files)]

def valor_maxim(matriu):
    return max(max(fila) for fila in matriu)

def valor_minim(matriu):
    return min(min(fila) for fila in matriu)

# Exemple d'ús
files = 3
columnes = 3
matriu = crear_matriu_aleatoria(files, columnes)
print("Matriu Aleatòria:", matriu)
print("Valor màxim:", valor_maxim(matriu))
print("Valor mínim:", valor_minim(matriu))
