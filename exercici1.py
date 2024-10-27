def crear_matriu_diagonal():
    # Crear una matriu 7x7 amb 0s i només valors ascendents a la diagonal
    matriu = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        matriu[i][i] = i * 7  # Els valors seran de 0 a 49 de 7 en 7
    return matriu

def guardar_matriu(matriu, filename):
    # Guardar la matriu en un fitxer de text
    with open(filename, 'w') as file:
        for row in matriu:
            file.write(" ".join(map(str, row)) + "\n")

# Executa la funció i guarda la matriu
matriu = crear_matriu_diagonal()
guardar_matriu(matriu, "exercici1.txt")
